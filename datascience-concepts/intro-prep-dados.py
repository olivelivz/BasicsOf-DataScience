import pandas as pd

df = pd.read_csv('L:/Lívia Oliveira/Programas/vivaldi/clientes-v2')

print(df.head().to_string())
print(df.tail().to_string())

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print("Verificacao inicial\n")
print(df.info)

print('Analise de dados nulos:\n',(df.isnull().sum()))
print('% de dados nulos:\n',(df.isnull().mean()*100))
df.dropna(inplace=True)

print('Confirmar remoção de dados\n', df.isnull().sum().sum())

print('Analise de dados duplicados\n', df.duplicated().sum())

print('Analise de dados unicos\n', df.unique().sum())

print('Estatitica de dados\n', df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)