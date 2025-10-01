"""
012 Faça um algoritmo que leia o preço de um produto e
mostre o seu novo preço com 5% de desconto.
"""
print('========================')
print('==== 5% DE DESCONTO ====')
print('========================\n')
desconto = 0.05
precoProduto = float(input('Digite o proço do produto R$ '))
valorDesconto = precoProduto * desconto
precoDescontado = precoProduto - valorDesconto
print(f'Valor com desconto RS {precoDescontado:.2f} reias.')




