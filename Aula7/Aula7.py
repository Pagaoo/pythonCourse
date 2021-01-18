"""
Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa.
Criar variável com o ano atual (int) e obter ano de nascimento com base na idade no ano atual.
Obter IMC da pessoas com apenas duas casas decimais.
Exibir o texto com f - strings
"""
nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
mes = int(input('Qual mes em numeros tu nasceu? '))
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual seu peso? '))
ano_atual = 2021
mes_atual = 2

IMC = peso / altura ** 2
ano_nascimento = 2019 - idade
if mes_atual > 2:
    ano_nascimento = ano_nascimento
else:
    ano_nascimento = ano_nascimento + 1

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é de: {IMC:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
