"""
017 Faça um programa que leia o comprimento do cateto oposto e do
 cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

"""
from math import sqrt, pow
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('^^ COMPRIMENTO DA HIPOTENUSA ^^')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
catetoOposto = int(input('Quanto mede o cateto oposto? '))
catetoAdjacente = int(input('Qual a medida do cateto adjacente? '))
comprimentoCatetos = (catetoOposto ** 2) + (catetoAdjacente ** 2)
hipotenusa = sqrt(comprimentoCatetos)
print(f'Comprimento da hipotenusa = {hipotenusa:.3f}\n'
      f'Cateto oposto = {catetoOposto:.3f}\n'
      f'Cateto adjacente = {catetoAdjacente:.3f}'
)

