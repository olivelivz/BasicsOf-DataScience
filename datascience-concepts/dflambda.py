import pandas as pd

# funcao para calcular o cubo de n
def eleva_cubo(x):
    return x ** 3

# expressao lambda para calcular o cubo
eleva_lambda = lambda x: x ** 3
print(eleva_lambda(2))


# criacao do dataframe e popularização
df = pd.DataFrame({'numeros' : [1, 2, 3, 4, 5, 10]})

# aplicando funcao eleva_cubo ao dataframe
df['eleva_cubo'] = df['numeros'].apply(eleva_cubo)

# ou seja, tres ou 4 linhas apenas para aplicar o cubo ao dt

#/---------------------------------------------------------\

# aplicando o lambda ao dataframe
df['eleva_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)
