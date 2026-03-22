"""
Faça um programa que leia um número qualquer e moostre o seu fatorial.

Ex.: 5º = 5*4*3*2*1 = 120

"""
"""from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} = {f}')"""

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')

