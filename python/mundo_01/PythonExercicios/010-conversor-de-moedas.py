"""
    Crie um programa que leia quanto dinheiro uma pessoa
    tem na carteira e mostre quantos dólares ela pode comprar.
    Considere
    US$ 1,00 = R$ 4,93
"""
cotacaoDolar = 4.93
cotacaoEuro = 5.38

nome = input('Qual o seu nome? ')
totalDinehiroCarteira = float(input('Quanto dinheiro tem na carteira? R$ '))

comprarDolares = totalDinehiroCarteira / cotacaoDolar
comprarEuro = totalDinehiroCarteira / cotacaoEuro

print(f'{nome}, com R$ {totalDinehiroCarteira:,.2f}, você pode comprar US$ {comprarDolares:,.2f} dólares.')
print(f'{nome}, com R$ {totalDinehiroCarteira:,.2f}, você pode comprar £ {comprarEuro:,.2f} euros.')
