"""
Escreva um programa para apovar o empréstimo bancário para a compra de uma casa.

O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em quantos anos ele vai pogar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
print('-=-=-=-=-' * 5)
print('         FINANCIAMENTO IMOBILIÁRIO')
print('-=-=-=-=-' * 5)

nomeComprador = str(input('\nBEM-VINDO(A)! Me diz seu nome: '))
valorCasa = float(input(f'Olá {nomeComprador}!\nQual o valor da casa R$ '))
salarioAtual = float(input('Quanto você ganha por mês R$ '))
anosPagamento = int(input('Em quantos anos pretende pagar? '))
anoEmMeses = anosPagamento * 12
print(anoEmMeses)
prestacaoExcedente = (salarioAtual * 30) / 100
valorPrestacao = valorCasa / anoEmMeses

print(f'{valorPrestacao:.2f}')

# FALTA A CONDIÇÃO PARA LIBERAR OU NÃO O FINANCIAMENTO
