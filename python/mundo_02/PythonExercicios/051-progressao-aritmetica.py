"""
Desenvolva um programa que leia o PRIMEIRO termo e
a razão de uma P.A. (progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 21)
print('10 TERMOS DE UMA P.A.')
print('=' * 21)
primeiroTermo = int(input('1º termo: '))
razao = int(input('Razão: '))
enesimoTermo = primeiroTermo + (10 - 1) * razao
for PA in range(primeiroTermo, enesimoTermo, razao):
    print(f'{PA}', end=' -> ')
print('ACABOU')













