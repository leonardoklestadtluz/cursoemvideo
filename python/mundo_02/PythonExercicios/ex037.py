"""

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO.

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
print('\n*** Escolha uma opção ***\n1 - Base binária \n2 - Base octal\n3 - Base hexadecimal\n')
opcaoConversao = int(input('Opção? '))
if opcaoConversao == 1:
    print(f'\nNúmero {numero}, representado em base Binária: {baseBinaria}')
elif opcaoConversao == 2:
    print(f'\nNúmero {numero}, representado em base Octal: {baseOctal}')
else:
    print(f'\nNúmero {numero}, representado em base Hexadecimal: {baseHexadecimal}')
