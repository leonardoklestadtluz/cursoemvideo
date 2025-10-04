""" 013 Faça um algoritmo que leia o salário de um
funcionário e mostre o seu novo salário com 15% de aumento.
"""
print('========================')
print('==== NOVO SALÁRIO ====')
print('========================\n')
nome = input('Me diga seu nome: ')
salario = float(input('Diga qual é seu salário R$ '))
aumento = salario * 0.15
novoSalario = salario + aumento
print(f'Olá {nome}! Este é seu novo salário R$ {novoSalario}')
