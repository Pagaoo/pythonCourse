"""
Varáveis podem ser separadas por _, conter números, letras maiúsculas ou minúsculas e não podem ser iniciadas
por números, somente letras.
"""

nome = 'Gabriel'  # str
idade = 21  # int
altura = 1.76  # float
maior_idade = idade > 18  # bool

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?', maior_idade)
peso = 65  # int

imc = peso / altura ** 2
imc_2casas = "{:.2f}".format(imc)

print(nome, 'tem', idade, 'anos de idade e possui imc de:', imc_2casas)
