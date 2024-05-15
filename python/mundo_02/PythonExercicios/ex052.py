"""
Faça um programa que leia um NÚMERO INTEIRO e
diga se ele é ou não um NÚMERO PRIMO.
"""
print('=' * 21)
print('NÚMEROS PRIMOS')
print('=' * 21)
numero = int(input("Digite um número: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\nO número {numero} foi divisível {total} vezes.')
if total == 2:
    print(f'Número {numero} É primo.')
else:
    print(f'Número {numero} NÃO é primo.')
