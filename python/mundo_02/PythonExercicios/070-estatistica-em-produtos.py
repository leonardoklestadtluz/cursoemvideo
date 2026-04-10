"""

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.

No final, mostre:

A. qual é o total gasto na compra?

B. quantos produtos custam mais de R$ 1.000,00?

C. qual é o nome do produto mais barato?
"""
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
totalCompra = totMaior1000 = menorPreco = cont = 0
prodMaisBarato = ''
while True:
    nomeProduto = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Preço do produto R$ '))
    cont += 1
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        prodMaisBarato = nomeProduto
    totalCompra += preco
    if preco > 1000:
        totMaior1000 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Mais algum produto? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'Total das compras R$ {totalCompra:.2f}')
print(f'Custou mais de R$ 1.000,00 = {totMaior1000} produto(s).')
print(f'{prodMaisBarato} é o produto mais barato. Custou R$ {menorPreco:.2f}.')
