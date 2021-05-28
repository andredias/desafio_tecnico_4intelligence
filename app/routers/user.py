from fastapi import APIRouter, HTTPException
from loguru import logger

from ..models import User, UserIn

router = APIRouter()
users: dict[str, User] = {}


@router.get('/users', response_model=list[User])
async def get_users():
    logger.debug(users)
    return [u for u in users.values()]


@router.get('/users/{cpf}', response_model=User)
async def get_user(cpf: str):
    if cpf not in users:
        raise HTTPException(404)
    return users[cpf]


@router.post('/users', status_code=201)
async def include_user(user: User):
    logger.debug(user)
    users[user.cpf] = user
    return


@router.put('/users', status_code=204)
async def update_user(user: UserIn):
    logger.debug(user.dict(exclude_unset=True))
    if user.cpf not in users:
        raise HTTPException(404)
    data = user.dict(exclude_unset=True, exclude_none=True)
    users[user.cpf] = users[user.cpf].copy(update=data)
    return


@router.delete('/users/{cpf}', status_code=204)
async def delete_user(cpf: str):
    if cpf not in users:
        raise HTTPException(404)
    del users[cpf]
    return
