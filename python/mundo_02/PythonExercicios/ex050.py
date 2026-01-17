"""
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES.
Se o valor digitado for ÍMPAR, desconsidere-o.
"""
print('=' * 14)
print('SOMA DOS PARES')
print('=' * 14)
somaPar = 0
numOrdinal = 0
for numero in range(0, 6):
    numOrdinal += 1
    numero = int(input(f'Digite o {numOrdinal}º número: '))
    if numero % 2 == 0:
        somaPar += numero
print('=' * 14)
print(f'\nSomatório dos numeros pares = {somaPar}.')
