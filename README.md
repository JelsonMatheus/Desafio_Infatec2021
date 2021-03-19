# Desafio Infatec - 2021
Home Page | Tela login
--------- | -----------
<img src="print.jpg"> | <img src="print2.jpg">

<br>
Sistema para gestão escolar no qual poderá realizar
cadastro de alunos, professores, turmas e gerar relatórios.

## Tecnologias usadas:
* Html
* CSS, Bootstrap
* javascript
* Python, Django


# Configurações:

Para rodar um servidor local Django e utilizar a aplicação será nescessario seguir as seguintes etapas.

1 - Criar o ambiente virtual para instalar as dependencias do projeto.
  ```sh
  pyton -m venv venv
  ```

2 - Ativar o ambiente virtual.
- windows -
  ```sh
  venv\scripts\activate
  ```

3 - Instalar as dependencias.
  ```sh
  pip install -r .\requirements.txt
  ```

Com as configurações de dependências feitas, no repositório do projeto
já existe um banco de dados, **apenas** para teste, com dados pre-cadastrados. 
Basta inicializar o servidor:

1 - Iniciar servidor Django
  ```sh
  python manage.py runserver
  ```
  ```sh
  System check identified no issues (0 silenced).
  February 15, 2021 - 13:31:53
  Django version 3.1.6, using settings 'config.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```

2 - O servidor será iniciado em localhost:8000
- Os path seguem apartir dai.

Caso não utilize o banco de dados, você deve seguir os procedimentos:

1 - Realizar o makemigrations e migrate
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```

2 - Criar um superuser com nome admin:
  ```sh
  python manage.py createsuperuser --username admin**
  Email address: example@mail.com**
  Password: ******
  Password(again): ******
  ```
  - confirme se necessário.

3 - Inicializar seguindo os passos já descritos.

4 - Realizar o login e acessar *path:* /admin/
- Realize o cadastro de uma escola e series manualmente pelo Django admin.

5 - A partir daí você pode voltar a página principal da aplicação.

## Path para consulta de dados:
* /relatorio/consulta-alunos/
  - Retorna um **json** que contém uma lista de aluno.ch
    ```json
    }
        "alunos" : [
            {
                "nome" : "nome", 
                "serie" : "serie"
            }, 
         ]
    }
    ```

* /relatorio/consulta-professores/
  - Retorna um **json** que contém uma lista de professores.
    ```json
    {
        "professores": [
            {
                "nome'": "nome", 
                "turma": 'turma"
            }, 
         ]
    }
    ```

* /relatorio/consulta-turma/ ou /relatorio/consulta-turma/<serie_id>/
  - Retorna um **json** com uma lista de turmas.
    ```json
    {
        "turmas" : [
            {
                "nome" : "nome",
                "series" : [ ],
                "id" : "turma_id"
            },
      ]
    }
    ```

## Observações:
* Os dados no banco de dados são todos fictícios e são usados
apenas para testes.


