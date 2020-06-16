def somaImposto(taxaImposto, custo):
    return (1 +taxaImposto/100)*custo

taxaImposto = int(input('Insira a porcetagem de imposto: '))
custo = float(input('Digite o valor do produto: '))

print(f'O valor do produto com a taxa de imposto é: {somaImposto(taxaImposto,custo)}')