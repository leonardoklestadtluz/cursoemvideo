"""
  Escreva um programa que converta uma temperatura digitada em ºC e converta-a para ºF.

  Fórmula: (40 °C × 1,8) + 32 = 104 °F

  Retorno: A temperatura de 31.5ºC corresponde a 88.7ºF!
"""
tempCelsius = float(input('Informe a temperatura em ºC: '))
tempConvertidaF = (tempCelsius * 1.8) + 32
print(f'A temperatura de {tempCelsius}ºC, corresponde a {tempConvertidaF:,.2f}ºF!')

