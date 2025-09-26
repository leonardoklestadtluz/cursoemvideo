#008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print('\n***** CONVERTER MEDIDAS *****\n')
metros = float(input('Informe uma medida em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'Centímetros {centimetros:.2f} \nMílímetros {milimetros:.2f}')
