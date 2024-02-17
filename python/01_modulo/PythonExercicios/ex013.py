"""
    Faça um algoritmo que leia o salário de um funcionário
    e motre seu novo salário com 15% de aumento.
"""
salarioAtual = float(input('Infrme seu salário R$ '))
aumento = salarioAtual * 0.15
novoSalario = salarioAtual + aumento
print(f'Seu novo salário R$ {novoSalario:,.2f} com 15% de aumento.')
