def argumentos(variavel):
    if variavel == 0 or variavel < 0:
        return 'N'
    else:
        return 'P'

variavel = int(input('Escreva algum número: '))

print(argumentos(variavel))