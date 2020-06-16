def printar_linha(n):
    for p in range(1,n + 1):
        print(f'{p}', end='')
    print()


def repetir_soma(n):
    for n in range(n+1):
        printar_linha(n)


n = int(input('Infome um número: '))

repetir_soma(n)