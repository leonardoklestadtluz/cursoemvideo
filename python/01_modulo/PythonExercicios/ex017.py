"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot

catetoOposto = float(input('Qual o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Qual o comprimento do cateto adjacente: '))
comprimentoHipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'Este é o comprimento da hipotenusa: {comprimentoHipotenusa:,.2f}')

