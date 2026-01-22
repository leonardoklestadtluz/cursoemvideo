"""
    Faça um algortimo que leia o preço de um produto
    e mostre seu novo preço, com 5% de desconto.
"""
nome = input('Qual é o seu nome? ')
precoOriginal = float(input('Informe o valor de um produto R$ '))

desconto = 0.05
valorComDesconto = precoOriginal * desconto
valorTotal = precoOriginal - valorComDesconto

print(f'Valor total R$ {valorTotal:,.2f}')
print(f'Parabéns {nome}! Você ganhou R$ {valorComDesconto:,.2f} (5%) de desconto em sua compra!')
