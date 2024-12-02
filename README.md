# Django Agenda de Contatos 📒🔒

Este repositório contém um projeto didático de uma agenda de contatos, desenvolvido com Django,
como parte de um curso de Python ministrado por Otávio Miranda. 
O sistema permite que usuários gerenciem seus contatos pessoais com segurança, utilizando autenticação via login.

## 📚 Recursos do Projeto

    Gerenciamento de Contatos:
        Adicionar, editar e excluir contatos.
        Armazenamento seguro e acessível apenas pelo usuário autenticado.
    Autenticação:
        Registro, login e logout.
        Cada usuário tem acesso apenas aos seus próprios contatos.
    Busca de Contatos:
        Filtragem e pesquisa fácil com base no nome ou outras informações.
    Interface Simples e Funcional:
        Design responsivo e fácil de usar.

## 🚀 Tecnologias Utilizadas

    Python 3.11+
    Django 4.0+
    SQLite: Banco de dados local para simplicidade no desenvolvimento.
    HTML, CSS e JavaScript para o front-end.

<br>

## ⚙️ Como Usar

  1. Clonar o Repositório Clone este repositório para sua máquina local:
    
    git clone https://github.com/Merctxt/Django_agenda.git
    cd Django_agenda

<br>

2. Configurar o Ambiente Virtual Crie e ative um ambiente virtual para o projeto:
   ```bash
   
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

<br>

3. Instalar Dependências Instale todas as dependências necessárias:
    ```bash
    
    pip install -r requirements.txt

<br>

4. Aplicar Migrações Configure o banco de dados local:
    ```bash
    
    python manage.py migrate

<br>

5. Iniciar o Servidor Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver

<br>

6. Acessar no Navegador Abra o navegador e acesse:
    ```bash
   http://127.0.0.1:8000

---

<br>

## 📝 Licença

Este projeto está licenciado sob os termos da [Licença MIT](./LICENSE). 
Sinta-se à vontade para explorar e modificar.

<br>

## 🙌 Agradecimentos

Este projeto é parte do curso de Python ministrado por Otávio Miranda.
