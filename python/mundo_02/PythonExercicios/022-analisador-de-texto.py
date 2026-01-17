"""

Crie um programa que leia o nome completo de uma pessoa e mostre:

    [x] o nome com todas as letras maiúsculas
    [x] o nome com todas as letras minúsculas
    [x] quantidade de letras ao todo (sem considerar espaços)
    [x] quantas letras tem o primeiro nome
"""
nome = str(input('Digite seu nome completo: '))
print(f'Todas as letras maiúsculas: {nome.upper()}')
print(f'Todas as letras minúsculas: {nome.lower()}')
print(f'Total de letras do nome completo: {len(nome.replace(" ", ""))}')
print(f'Total de letras do primeiro nome: {len(nome.split()[0])}')



