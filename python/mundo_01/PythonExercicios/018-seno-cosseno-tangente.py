"""

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians

anguloQualquer = float(input('Qual é o ângulo ? '))
seno = sin(radians(anguloQualquer))
cosseno = cos(radians(anguloQualquer))
tangente = tan(radians(anguloQualquer))
print(f'Seno: {seno:,.2f} | Cosseno: {cosseno:,.2f} | Tangente: {tangente:,.2f}')


