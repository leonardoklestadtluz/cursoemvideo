
from datetime import date
"""

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""

print('_-_' * 6)
print('| ANO BISSEXTO |')
print('_-_' * 6)

ano = int(input('\nQue ano quer analisar? Digite 0 para analisar o ano atual. '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é bissexto.')
else:
    print(f'Ano {ano} NÃO é bissexto.')







