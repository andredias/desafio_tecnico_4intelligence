
Desafio Técnico 4intelligence
=============================

Criar uma API REST utilizando FastAPI e/ou Django para cadastro de usuários
e integrá-la ao banco de dados de sua escolha.
É fundamental ter validação de input na inserção de dados.
Também é recomendado que o código seja desenvolvido orientado a teste (TDD)
e os *commits* sejam progressivos afim de demonstrar a evolução do código.

Para cada usuário deve-se ter os seguintes dados:

* Nome
* Data de nascimento
* CPF (com validação se é um CPF é válido e permitirapenas umcadastro por CPF)
* Endereço

  * CEP (Validar se é válido e, se possível, autopreencher os demais campos)
  * Rua
  * Bairro
  * Cidade
  * Estado

Criar endpoints para:

* Atualizar dados de um usuário existente
* Remover um usuário cadastrado
* Listar todos os usuários
* Listar todas as informações de um usuário específico

Cada *endpoint* deve retornar seu código HTTP de acordo com o resultado da  requisição,
exemplo:

* 404 quando tentar acessar informações de um usuário não existente
* 200 quando tiver sucesso na solicitação.


Pontos Extras (não-obrigatórios)
--------------------------------

* Deploy da API
* JWT
* Executar via Docker
* Utilizar Postgres como DB
* Documentação

Enviar as collections do Postman para fazermos a validação dos endpoints e
o link do repositório público para avaliação do teste.
