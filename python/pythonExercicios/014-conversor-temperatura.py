"""

014 Escreva um programa que converta uma temperatura digitada em graus celsius para fahrenheit.

"""
print('====================================')
print('==== CONVERSOR DE TEMPERATURA ======')
print('====================================\n')
temperatura = float(input('Temperatura? '))
temperaturaConvertida = temperatura * 1.8 + 32
print(f'A temperatura de {temperatura:.2f}ºC corresponde a {temperaturaConvertida:.2f}ºF')