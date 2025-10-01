"""
010 Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.

Considere U$$ 1,00 = R$ 5,32
"""
print('=======================')
print('==== COMPRAR DÓLAR ====')
print('=======================\n')
dinheiroCarteira = float(input('Quanto R$ tem na carteira? '))
valorDolaR = 5.32
quantidadeDolar = dinheiroCarteira / valorDolaR
print(f'Com R$ {dinheiroCarteira:.2f} reais, você compra US$ {quantidadeDolar:.2f} dólares.')
