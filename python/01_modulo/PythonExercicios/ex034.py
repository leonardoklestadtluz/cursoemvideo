"""

Escreva um programa que pergunte o salário de um funcionário.
Calcule o valor de seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, aumento é de até 15%.

"""
print('$$-$$' * 6)
print('  $$$ Aumentos Múltiplos $$$')
print('$$-$$' * 6)
salarioAtual = float(input('\nQuanto você ganha por mês R$? '))
maiorQue1250 = ((salarioAtual * 10) / 100)
menorIgual1250 = ((salarioAtual * 15) / 100)
salarioNovo = salarioAtual
valorAumento = 0.00
if salarioNovo <= 1250:
    salarioNovo = salarioAtual + menorIgual1250
    valorAumento = menorIgual1250
else:
    salarioNovo = salarioAtual + maiorQue1250
    valorAumento = maiorQue1250
print(f'\nPARABÉNS!! Seu novo salário é R$ {salarioNovo:.2f}.'
      f'\nSeu salário teve um aumento no valor de R$ {valorAumento:.2f}.')

