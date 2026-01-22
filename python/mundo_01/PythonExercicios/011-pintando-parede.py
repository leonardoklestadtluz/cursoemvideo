"""
    Faça um programa que leia a largura e altura de uma parede em metros,
    calcule a sua área e a quantidade de tinta necessária para pintá-la,
    sabendo que cada litro de tinta, pinta uma área de 2m².
"""
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
totalTinta = area / 2
# print(f'Área da parede = {area:,.2f} m².')
# print(f'Precisamos de {totalTinta:,.2f} L.')
print(f'Com essas dimensões {altura:,.2f}m² x {largura:,.2f}m², precisamos de {totalTinta:,.2f} litros de tinta.')
