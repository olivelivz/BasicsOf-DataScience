class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    idade = 15

    def saudacao(self):
        print('Olá Pessoas!')

# Criando um objeto da classe Pessoa
matheus = Pessoa()

# Acessando o atributo idade
print(matheus.idade)  # Saída: 15

# Acessando o método saudacao sem os parênteses (referência ao método)
print(matheus.saudacao)  # Saída: <bound method Pessoa.saudacao of <__main__.Pessoa object at ...>>

# Chamando o método saudacao (com parênteses)
matheus.saudacao()  # Saída: Olá Pessoas!
