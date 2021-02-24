"""
For in em Python
Iterando str com for
Função range(start=0, stop, step=1), O step seta como o for vai contar, de 1 em 1, 2 em 2 ...
"""

texto = 'Python e Javascript'
texto_1 = 'Python e Javascript'
novo_texto = ''

for i, letra in enumerate(texto):  # Enumera os indexes da str
    print(i, letra)

print('-'*35)

for letter in texto_1:
    if letter == 't':
        novo_texto += letter.upper()
    elif letter == 'a':
        novo_texto += letter.upper()
    elif letter == 'h':
        novo_texto += letter.upper()
    else:
        novo_texto += letter
print(novo_texto)

print('-'*35)

for n in range(0, 10, 3):
    print(n)

print('-'*35)

for n in range(100):
    if n % 8 == 0:
        print(n)  # Essa função if, seria a mesma coisa que usar o step de 8 numa contagem de 0 - 99
