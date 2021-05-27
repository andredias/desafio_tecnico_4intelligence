from pytest import raises

from app.models import User
from app.utils import remove_symbols


def test_remove_symbols():
    assert remove_symbols('123.456.789-01') == '12345678901'


def test_valida_cep():
    cep = '123.456-120'
    with raises(ValueError):
        User.valida_cep(cep)

    cep = '12.345-678'
    assert User.valida_cep(cep) == '12345678'


def test_valida_uf():
    uf = '12'
    with raises(ValueError):
        User.valida_uf(uf)

    uf = 'O+'
    with raises(ValueError):
        User.valida_uf(uf)

    uf = 'Sp'
    assert User.valida_uf(uf) == 'SP'


def test_valida_cpf():
    cpf = '123.456.-:/'
    with raises(ValueError, match='CPF deve ter 11 digitos'):
        User.valida_cpf(cpf)

    cpf = '111.111.111-11'
    with raises(ValueError, match=f'{remove_symbols(cpf)} não é um valor válido'):
        User.valida_cpf(cpf)

    cpf = '123.456.789-01'
    with raises(ValueError, match=f'{remove_symbols(cpf)} não é um valor válido'):
        User.valida_cpf(cpf)

    assert User.valida_cpf('529.982.247-25') == '52998224725'
