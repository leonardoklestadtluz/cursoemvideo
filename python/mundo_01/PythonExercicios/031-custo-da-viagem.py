"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.

Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
de até 200Km e R$ 0,45 para viagens mais longas.

"""
print('_#_' * 8)
print('$$$ CUSTO DA VIAGEM $$$')
print('_#_' * 8)

distancia = float(input('\nQual a distância da viagem em Km? '))
distanciaInformada = f'Distância: {distancia:.2f} Km.'
precoAte200 = distancia * 0.50
precoViagemLonga = distancia * 0.45

preco = precoAte200 if distancia <= 200 else precoViagemLonga

# if simplificado
print(f'Distância informada: {distancia:.2f} Km.\nValor total R$ {preco:.2f}.')

"""
if distancia <= 200:
    print(distanciaInformada)
    print(f'Valor total R$ {precoAte200:.2f}.')
else:
    print(distanciaInformada)
    print(f'Valor total R$ {precoViagemLonga:.2f}.')
"""

