"""
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado.

    Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
"""
print('=' * 30)

print('=== INFORMAÇÕES DO ALUGUEL ===')
kmRodado = 0.15
diaria = 60.00
qtdDiasAlugados = int(input('Quantos dias de aluguel? '))
qtdKmPercorrido = float(input('Quantos km percorridos? '))

valorTotalKmPercorrido = qtdKmPercorrido * kmRodado
valorTtotalDiasAluguel = qtdDiasAlugados * diaria
valorTotalPagar = valorTotalKmPercorrido + valorTtotalDiasAluguel

print(f'Km percorridos: {qtdKmPercorrido:,.2f} km.')
print(f'Dias alugados: {qtdDiasAlugados} dias.')
print('=== INFORMAÇÕES DO ALUGUEL ===\n')

print('-' * 20)

print('\n=== INFORMAÇÕES DE PAGAMENTO ===')
print(f'Total a pagar: R$ {valorTotalPagar:,.2f}')
print('=== INFORMAÇÕES DE PAGAMENTO ===')

print('=' * 30)
