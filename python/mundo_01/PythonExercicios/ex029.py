"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

* A multa vai custar R$ 7,00 por cada Km acima do limite.

"""
print('--&--' * 5)
print('*** RADAR ELETRÔNICO ***')
print('--&--' * 5)

velocidadeAtual = float(input('\nQual a velocidade do carro? '))
velocidadeMaxima = 80
valorKmExcedente = 7
valorTotalMulta = (velocidadeAtual - velocidadeMaxima) * valorKmExcedente

if velocidadeAtual > velocidadeMaxima:
    print(f'MULTADO! Você excedeu o limite máximo de {velocidadeMaxima} Km/h da via.')
    print(f'Valor a pagar R$ {valorTotalMulta:.2f}')
else:
    print(f'Sua velocidade: {velocidadeAtual} Km/h. \nTenha um bom dia! Dirija com segurança.')



