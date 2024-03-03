"""

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""
print('-#-' * 6)
print('@@ PAR ou ÍMPAR @@')
print('-#-' * 6)

numero = int(input('\nDigite um número: '))
resultado = numero % 2 == 0

if resultado:
    print(f'Número {numero} é PAR!')
else:
    print(f'Número {numero} é ÍMPAR!')


