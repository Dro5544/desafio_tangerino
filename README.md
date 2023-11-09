# Desafio Tangerino
Segue a minha resolução do case para a vaga de Administrador de Banco de Dados.

### Requisitos
- Python 3.12
- Docker

### Instruções
- Abrir o terminal na pasta do projeto
- criação do ambiente virtual: `python -m venv venv`
- ativar o venv: `.\venv\Scripts\activate`
- instalar dependências: 
  - `pip install -r requirements_win.txt` no WINDOWS
  - `pip install -r requirements_linux.txt` no LINUX
- inicar docker: `docker compose up -d`
- criação dos dados mockados: `python mock_database.py`
- execução do etl: `python sql_job.py`

### Respostas
- As respostas apareceção no terminal com a execão do sql_job.py