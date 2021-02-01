"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva:
'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva: 'Seu nome é normal'; se maior que 6, escreva:
'Seu nome é muito grande'
"""
primeiro_nome = input('Digite seu primeiro nome: ')
tamanho = len(primeiro_nome)

if tamanho <= 4:
    print(f'O nome {primeiro_nome} é curto')
elif 5 <= tamanho <= 6:
    print(f'O nome {primeiro_nome} é normal')
else:
    print(f'O nome {primeiro_nome} é muito grande')
