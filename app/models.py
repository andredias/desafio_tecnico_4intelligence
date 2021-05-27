from datetime import date
from string import ascii_letters

from pydantic import BaseModel, validator

from .utils import remove_symbols


class Endereco(BaseModel):
    logradouro: str
    bairro: str
    cidade: str
    uf: str
    cep: str

    @validator('cep')
    def valida_cep(cls, value: str) -> str:  # noqa: N805
        cep = remove_symbols(value)
        if len(cep) != 8:
            raise ValueError(f'{cep} não é um CEP válido')
        return cep

    @validator('uf')
    def valida_uf(cls, value: str) -> str:  # noqa: N805
        if len(value) != 2 or any(True for v in value if v not in ascii_letters):
            raise ValueError(f'{value} não é um valor válido')
        return value.upper()


class User(Endereco):
    cpf: str
    nome: str
    nascimento: date

    @validator('cpf')
    def valida_cpf(cls, value: str) -> str:  # noqa: N805
        cpf = remove_symbols(value)
        if len(cpf) != 11:
            raise ValueError('CPF deve ter 11 digitos')

        error_msg = f'{cpf} não é um valor válido'

        # validação de dígitos repetidos
        if cpf == (cpf[0] * 11):
            raise ValueError(error_msg)

        # valida primeiro dígito
        sum = 0
        for i in range(9):
            sum += int(cpf[i]) * (10 - i)
        remaining = (sum * 10) % 11
        if remaining == 10:
            remaining = 0
        if str(remaining) != cpf[-2]:
            raise ValueError(error_msg)

        # valida segundo dígito
        sum = 0
        for i in range(10):
            sum += int(cpf[i]) * (11 - i)
        remaining = (sum * 10) % 11
        if str(remaining) != cpf[-1]:
            raise ValueError(error_msg)

        return cpf
