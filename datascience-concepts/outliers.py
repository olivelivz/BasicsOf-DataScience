import pandas as pd
from scipy import stats

df = pd.read_csv('L:/Lívia Oliveira/Programas/vivaldi/clientes.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro basico \n', df_filtro_basico[['nome', 'idade']])

#identificar com zscore
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >=3]
print('Outliers pelo Zscore:\n', outliers_z)

#filtrar outliers com zscore
df_zscore = df[(stats.zcore(df['idade']) < 3)]

#identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('Limites IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo | (df['idade'] > limite_alto))]
print('Outliers pelo IQR: \n', outliers_iqr)

#filtrar outliers com IQR
df_idade = df[(df['idade'] < limite_baixo & (df['idade'] > limite_alto))]

#filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço Invalido' if len(x.split('\n')) < 3 else x)

#tratar campos de texto
df['nome'] = df['nome'].aplly(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd registro com nomes grandes: ', (df['nome'] == 'Nome inválido').sum())

print('Dados com outliers tratados: \n', df)

#salvar dataframe
df.to_csv('clientes_remove_outliers.csv', index=False)