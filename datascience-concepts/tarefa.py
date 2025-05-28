import pandas as pd

df = pd.read_csv('/data/ecommerce.csv')

# Verifique a quantidade de linhas e colunas


linhas_colunas = ...
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = ...
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = ...
print('Verificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
...

