import pandas as pd
from sqlalchemy import create_engine

db_url_src = 'postgresql://postgres:12345@localhost/tangerino1'
db_url_dsc = 'postgresql://postgres:12345@localhost/tangerino2'

engine_src = create_engine(db_url_src)
engine_dsc = create_engine(db_url_dsc)

query_src = 'select * from t_ponto'

df = pd.read_sql(query_src,engine_src)

#print(df.head())

# 1- Quantidade de pontos por usuário
print('Questão 01')
print(df.groupby('usuario').count()['id'].reset_index())

# 2- Quantidade de pontos por empresa
print('Questão 02')
print(df.groupby('empresa').count()['id'].reset_index())

# 3- Usuários que tiveram mais ponto
print('Questão 03')
print(df.groupby('usuario').count()['id'].reset_index().sort_values('id',ascending=False)[:10])

# 4- Média diária de marcaçoes
print('Questão 04')
print(df.groupby('data').count()['id'].reset_index()['id'].mean())

df.to_sql('t_ponto_destino',engine_dsc, if_exists='replace') 