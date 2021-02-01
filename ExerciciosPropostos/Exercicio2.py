"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação
apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
import time, datetime

hora = input('Digite a hora (0 - 23): ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Digite a hora entre 0 - 23')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Digite um número entre 0 - 23')
