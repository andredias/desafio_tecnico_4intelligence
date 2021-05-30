Instruções
==========

O projeto pode ser executado diretamente a partir de containers:

1. ``docker-compose up``
2. Visite http://localhost:8000/docs
3. Teste a aplicação a partir dessa interface


Instalação
==========

O projeto depende da versão *3.9* do Python
e usa o poetry_ como gerenciador de dependências e de ambiente virtual.

Para instalar as dependências, execute::

    $ poetry install


Tarefas de Projeto
===================

As tarefas de projeto como ``run`` e ``test`` estão registradas no
`Makefile <Makefile>`_.

É necessário ativar o ambiente virtual antes de executar qualquer tarefa::

    $ poetry shell

Como alternativa,
é possível executar uma tarefa sem ativar o ambiente virtual antes.
Por exemplo::

    $ poetry run make test

Para rodar o projeto a partir do ambiente de desenvolvimento::

    $ make run

Para executar os testes::

    $ make test


.. _poetry: https://python-poetry.org/
