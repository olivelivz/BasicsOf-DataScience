import pandas as pd

df = pd.read_csv('L:/Lívia Oliveira/Programas/vivaldi/clientes.csv')

#primeiros registros

print(df.head().to_string())

print(df.tail().to_string())

# verifica a qtd de linhas e colunas
print("QTD: ", df.shape)
print("-----------------------------------------------------------")

# verificar tipos de dados
print("TIPAGEM :\n", df.dtypes)
print("-----------------------------------------------------------")

#checar valores nulos
print("NULOS: \n", df.isnull().sum())
print("-----------------------------------------------------------")
