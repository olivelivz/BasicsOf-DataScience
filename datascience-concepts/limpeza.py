import pandas as pd
df = pd.read_csv('L:/Lívia Oliveira/Programas/vivaldi/clientes.csv')

pd.set_option('display.width', None)
print(df.head())

print("############################################################################\n")

# remover dados
df.drop(labels='pais', axis=1, inplace=True) # coluna
df.drop(labels=2, axis=0, inplace=True) #linha

# normalizar campos de texto
df['none'] = df['none'].str.title() # primeira letra de cada palavra maiuscula
df['endereco'] = df['endereco'].str.lower() # tudo minusculo
df['Estado'] = df['estado'].str.strip.upper() # tudo maiusculo

# converter tipos de dados
df['idade'] = df['idade'].astype(int)

# tratar valores nulos (ausentes)
df_fillna = df.fillna(0) # substitui o campo nulo por 0
df_dropna = df.dropna() # remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4) # manter registro com no minimo X valores nulos
df = df.dropna(subset=['cpf']) # remover registros com CPF nulo

print('Valores nulos\n', df.isnull().sum())
print('Qtd de registros nulos com fillna', df_fillna.isnull().sum())
print('Qtd de registros nulos com dropna', df_dropna.isnull().sum())
print('Qtd de registros nulos com dropna4', df_dropna4.isnull().sum())

df.fillna(value={'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#tratar formato de dado
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#tratar dados duplicados
print('Qtd registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros removendo duplicadas: ', len(df))

print('Dados Limpos: \n', df)

