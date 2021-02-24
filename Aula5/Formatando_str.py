"""
Formatando valores com modificadores

:s - Textos (str)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(divisao)
print(f'{divisao:.2f}')
print(f'{num_1:0>9}')  # Adiciona casas até ter 9 casas, incluindo o número selecionado
print(f'{num_1:0>9.2f}')  # Terão 9 casas e as últimas serão separadas por ponto
print(f'{num_2:9>9}')
print(f'{num_2:9<9}')
print(f'{num_2:9^9}')
print('-'*50)

nome = 'Gabriel ALO'
sobrenome = 'Paganini'
print(f'{nome:#^50}')
nome_formatado = '{0:$^50} {1:%<50}'.format(nome, sobrenome)
print(nome_formatado)
print(nome.title())  # Primeira letter maiscúla E SE TIVER ALGUMA LETRA MAISCULA QUE NÃO SEJA A PRIMEIRA É CORRIGIDO
