"""
011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule
sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2m².
"""
print('=============================')
print('==== QUANTIDADE DE TINTA ====')
print('=============================\n')
largura = float(input('Informe a LARGURA da parede em m²: '))
altura = float(input('Agora informa a ALTURA da parede em m²: '))
areaParede = largura * altura
totalTinta = areaParede / 2
print(f'Para uma área de {areaParede:.2f}m² são necessários {totalTinta} litros de tinta.')


