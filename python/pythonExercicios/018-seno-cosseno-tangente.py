"""
018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno,
cosseno e tangente desse ângulo.

"""
from math import sin, cos, tan
anguloQualquer = float(input('Digite um ângulo: '))
seno = sin(anguloQualquer)
cosseno = cos(anguloQualquer)
tangente = tan(anguloQualquer)
print(
    f'Valor de Seno = {seno:.2f}º\n'
    f'Valor de Cosseno = {cosseno:.2f}º\n'
    f'Valor de Tangente =  {tangente:.2f}º\n'
)
