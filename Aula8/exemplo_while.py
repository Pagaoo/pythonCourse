operacao = True

while operacao:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um segundo número: ')
    operador = input('Escolha um operador: ')  # Apenass +, -, /, *

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar somente números')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido')

    operacao = False
print('Operação finalizada')
