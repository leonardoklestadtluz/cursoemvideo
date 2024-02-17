"""
    Escreva um programa  que leia um valor em metros
    e o exiba convertido em centímetros e milímetros.
"""
valor = float(input('Digite um valor: '))

milimetros = valor * 1000
centimetros = valor * 100
decimetro = valor * 10

quilometro = valor / 1000
hectrometro = valor / 100
decametro = valor / 10

print(f'Valor {valor} m, convertido em centímtros: {centimetros:,.2f} cm')
print(f'Valor {valor} m, convertido em milímetros: {milimetros:,.2f} mm')
print(f'Valor {valor} m, convertido em dcímetros: {decimetro:,.2f} dm')

print(f'Valor {valor} m, convertido em quilômetors: {quilometro} km')
print(f'Valor {valor} m, convertido em hectrômetro: {hectrometro:} hm')
print(f'Valor {valor} m convertido em decâmetros: {decametro:} dam')