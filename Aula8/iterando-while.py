frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)  # Vai contar os espaços como indexes
contador = 0
nova_frase = ''

print(frase)
input_usuario = input('Qual letra da frase acima você quer deixar maiúscula: ')

while contador < tamanho_frase:
    if frase[contador] == ' ':
        print('Espaço', contador)
    else:
        print(frase[contador], contador)

    if frase[contador] == input_usuario:
        nova_frase += input_usuario.upper()
    else:
        nova_frase += frase[contador]

    contador += 1
print(nova_frase)
