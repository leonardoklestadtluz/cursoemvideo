from time import sleep
"""
Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50.
"""
print('=-=' * 6)
print('CONTAGEM DE PARES')
print('=-=' * 6)
for n in range(1, 50+1):
    if n % 2 == 0:
        sleep(0.3)
        print(f'Número: {n}')
