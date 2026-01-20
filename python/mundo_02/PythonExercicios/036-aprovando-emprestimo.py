"""
Escreva um programa para apovar o empréstimo bancário para a compra de uma casa.

O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em quantos anos ele vai pogar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
print('=-=' * 8)
print('APROVANDO EMPRÉSTIMO')
print('=-=' * 8)
nomeComprador = str(input('\nBEM-VINDO(A)! Me diz seu nome: '))
valorCasa = float(input(f'Olá {nomeComprador}!\nQual o valor da seu imóvel R$ '))
salarioAtual = float(input('Quanto você ganha por mês R$ '))
anosPagamento = int(input('Em quantos anos pretende pagar? '))
anoEmMeses = anosPagamento * 12
percentualSalarial = (salarioAtual * 30) / 100
print(f'Prestação mensal R$ {percentualSalarial}')
valorPrestacao = valorCasa / anoEmMeses
if valorPrestacao < percentualSalarial:
    print('PARABÉNS! Empréstimo aprovado!')
else:
    print('Hum... Que pena! O valor da prestação compromete mais que 30% do seu salário.')
print(f'Valor mensal R$ {valorPrestacao:.2f}')


