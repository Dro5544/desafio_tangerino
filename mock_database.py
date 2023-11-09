import pandas as pd
from faker import Faker # cria uma instâcia de valores aleatório. Ex: endereço, nome pessoas, nome de empresas, etc 
from datetime import datetime
from sqlalchemy import create_engine

fake = Faker(['pt_BR']) # cria instância do faker
qtd_linhas = 10000

id = [i for i in range(qtd_linhas)]
data = [fake.date_between(start_date = datetime(2022,8,4)) for i in range(qtd_linhas)]
usuario = []
empresa = []
for i in range(qtd_linhas):
    usuario.append(fake.email())
    empresa.append(fake.company_id())

dados = {
    'id': id,
    'data': data,
    'usuario': usuario,
    'empresa': empresa,
}

df = pd.DataFrame(dados)

#BANCOS UTILIZADOS NO DESENVOLVIMENTO
#db_url_src = 'postgresql://postgres:senhasourcedb@18.226.52.33:10000/postgres'

db_url = 'postgresql://postgres:senhasourcedb@localhost:10000/postgres'
engine =  create_engine(db_url)

df.to_sql('t_ponto', engine, index=False,if_exists='replace')
