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

print(nome, 'tem', idade, 'anos de idade e possui imc de:', imc)
print(f'{nome} tem {idade} anos de idade e possui imc de: {imc:.2f}')  # f string
print('{0} tem {1} anos de idade e possui imc de: {2:.2f}'.format(nome, idade, imc))  # string utilizando format
