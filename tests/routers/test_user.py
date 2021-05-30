from faker import Faker
from httpx import AsyncClient
from pydantic import parse_obj_as
from pytest import fixture

from app.schemas import User, UserIn

fake = Faker(['pt_BR'])
SEED = 1
NUM_RECORDS = 3


def fake_user() -> User:
    return User(
        nome=fake.name(),
        cpf=fake.cpf(),
        nascimento=fake.date_of_birth(),
        logradouro=fake.street_address(),
        bairro=fake.bairro(),
        cidade=fake.city(),
        uf=fake.estado_sigla(),
        cep=fake.postcode(),
    )


@fixture
async def users(app) -> list[User]:
    from app.models.user import insert

    Faker.seed(SEED)
    result = []
    for _ in range(NUM_RECORDS):
        user = fake_user()
        await insert(user)
        result.append(user)
    return result


async def test_get_users(users: list[User], client: AsyncClient) -> None:
    resp = await client.get('/users')
    assert resp.status_code == 200
    assert parse_obj_as(list[User], resp.json()) == users


async def test_get_user(users: list[User], client: AsyncClient) -> None:
    resp = await client.get(f'/users/{users[2].cpf}')
    assert resp.status_code == 200
    data = User.parse_obj(resp.json())
    assert data == users[2]

    cpf = fake.cpf()
    resp = await client.get(f'/users/{cpf}')
    assert resp.status_code == 404


async def test_post_user(users: list[User], client: AsyncClient) -> None:
    new_user = fake_user()

    resp = await client.get('/users')
    data = parse_obj_as(list[User], resp.json())
    assert len(data) == len(users)
    assert new_user not in data

    resp = await client.post('/users', content=new_user.json())
    assert resp.status_code == 201

    resp = await client.get('/users')
    data = parse_obj_as(list[User], resp.json())
    assert new_user in data


async def test_delete_user(users: list[User], client: AsyncClient) -> None:
    cpf = users[1].cpf

    resp = await client.delete(f'/users/{cpf}')
    assert resp.status_code == 204

    resp = await client.get('/users')
    assert resp.status_code == 200
    assert len(users) - len(resp.json()) == 1

    cpf = fake.cpf()
    resp = await client.delete(f'/users/{cpf}')
    assert resp.status_code == 404


async def test_put_user(users: list[User], client: AsyncClient) -> None:
    cpf = users[1].cpf
    user = UserIn(cpf=cpf, cep=fake.postcode())
    resp = await client.put('/users', content=user.json(exclude_unset=True))
    assert resp.status_code == 204

    resp = await client.get(f'/users/{cpf}')
    data = User.parse_obj(resp.json())
    assert user.cep == data.cep

    user = UserIn(cpf=fake.cpf(), cep=fake.postcode())
    resp = await client.put('/users/', content=user.json(exclude_unset=True))
    assert resp.status_code == 404
