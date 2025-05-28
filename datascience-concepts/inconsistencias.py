 # mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}, ***.***-{cpf[2:]}')
#output : 624.***.***-29

 #corrigir dados
df['data'] = pd.to_datetime(df['data'], format='%y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1999-01-01'))

