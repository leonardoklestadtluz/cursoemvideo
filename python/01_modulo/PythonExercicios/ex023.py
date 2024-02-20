"""

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Exemplo:
    Digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1

isso >>> [0:4] <<< no final da linha da declaração da variável numero
permite a digitar mais que quatro números, mas considera somente
os 4 primeiros
"""
numero = input('Digite um número de 0 a 9999: ')[0:4]
print(f'Unidade: {int(numero[3:])}')
print(f'Dezena: {int(numero[2:3])}')
print(f'Centena: {int(numero[1:2])}')
print(f'Milhar: {int(numero[0:1])}')

