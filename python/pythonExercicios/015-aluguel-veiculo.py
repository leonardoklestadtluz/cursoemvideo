"""

015 Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado.

Calcule o preço a pagar, sabendo que o carro custa R$60/ dia e R$0,15/ km rodado.

"""
print('========================')
print('==== CALC ALUGUEL ======')
print('========================\n')
quilometroPercorrido = float(input('Km percorrido? '))
diasAlugado = int(input('Dias alugado? '))
valorDiaria = float(60.00)
valorKmRodado = float(0.15)
valorTotalDiaria = diasAlugado * valorDiaria
valorTotalKm = quilometroPercorrido * valorKmRodado
totalAPagar = valorTotalDiaria + valorTotalKm
print('$$$$$$$$$$$$$$$$$$$$$$$')
print(f'TOTAL A PAGAR R$ {totalAPagar:.2f}')
print('$$$$$$$$$$$$$$$$$$$$$$$\n')
print(f'Km percorrido: {quilometroPercorrido:.2f} quilômetros.\n')
print(f'Dias de aluguel: {diasAlugado} dias.\n')
print(f'Valor total da diária R$ {valorTotalDiaria:.2f}\n')
print(f'Valor total de KM percorrido R$ {valorTotalKm:.2f}')