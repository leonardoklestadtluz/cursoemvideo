"""

Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a BASE DE CONVERSÃO.

1 - para binário
2 - octal
3 - para hexadecimal
"""
print('_-' * 15)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-_' * 15)
numero = int(input('\nDigite um número qualquer: '))
baseBinaria = bin(numero)
baseOctal = oct(numero)
baseHexadecimal = hex(numero)
print('''
    *** Escolha uma opção *** 
    1 - Base binária 
    2 - Base octal
    3 - Base hexadecimal
''')
opcaoConversao = int(input('Opção? '))
if opcaoConversao == 1:
    print(f'\nNúmero {numero}, representado em base Binária: {baseBinaria[2:]}')
elif opcaoConversao == 2:
    print(f'\nNúmero {numero}, representado em base Octal: {baseOctal[2:]}')
elif opcaoConversao == 3:
    print(f'\nNúmero {numero}, representado em base Hexadecimal: {baseHexadecimal[2:]}')
else:
    print('Opção inválida! Tente novamente.')
