"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
from math import trunc

numeroReal = float(input('Digite um valor qualquer: '))
print(f'{trunc(numeroReal)} é a parte inteira do valor: {numeroReal} digitado.')

