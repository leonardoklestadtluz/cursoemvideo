"""

Desenvolva um programa que leia o comprimento de três retas.
E diga ao usuário se elas podem ou não formar um triângulo.

triângulo: a soma de duas retas é sempre menor que a terceira reta.

"""
print('=-==-=' * 5)
print('  Analisando Triângulos')
print('=-==-=' * 5)

linha01 = float(input('\nDigite a medida da 1ª linha: '))
linha02 = float(input('Digite a medida da 2ª linha: '))
linha03 = float(input('Digite a medida da 3ª linha: '))

if linha01 < linha02 + linha03 and linha02 < linha01 + linha03 and linha03 < linha01 + linha02:
    print('\nSIM, as linhas podem formar um triângulo!')
else:
    print('\nLamento. As linhas não podem formar um triângulo.')
