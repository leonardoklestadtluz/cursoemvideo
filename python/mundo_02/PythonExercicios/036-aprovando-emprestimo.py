"""
Escreva um programa para apovar o empréstimo bancário para a compra de uma casa.

O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em quantos anos ele vai pogar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
print('=-=' * 8)
print('APROVANDO EMPRÉSTIMO')
print('=-=' * 8)
nomeComprador = str(input('\nBEM-VINDO(A)! Me diz seu nome: '))
valorImovel = float(input(f'Olá {nomeComprador}!\nQual o valor do imóvel R$ '))
salarioAtual = float(input('Quanto você ganha por mês R$ '))
anosPagamento = int(input('Em quantos anos pretende pagar? '))
anosEmMeses = anosPagamento * 12 # conversão de anos em meses
percentualSalarial = (salarioAtual * 30) / 100 # percentual comprometido do salário
valorPrestacao = valorImovel / anosEmMeses
print(f'Prestação mensal R$ {valorPrestacao:.2f}')
if valorPrestacao < percentualSalarial:
    print('PARABÉNS! Empréstimo aprovado!')
else:
    print('Hum... Que pena! O valor da prestação compromete mais que 30% do seu salário.')