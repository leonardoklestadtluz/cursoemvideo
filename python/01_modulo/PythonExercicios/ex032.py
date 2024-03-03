
from calendar import isleap
"""

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""

print('_-_' * 6)
print('| ANO BISSEXTO |')
print('_-_' * 6)

ano = int(input('Digite e um ano qualquer: '))
anoInformado = ano % 2 == 0

if ano == anoInformado:
    print(f'Ano {ano} é bissexto.')
else:
    print(f'Ano {ano} NÃO é bissexto.')







