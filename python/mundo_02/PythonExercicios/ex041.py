from datetime import date
"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade.

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SÊNIOR
- acima: MASTER

"""
print('=-=' * 10)
print('CLASSIFICANDO ATLETAS')
print('=-=' * 10)
anoNascimento = int(input('Em que ano o atleta nasceu? '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print(f'O atleta tem {idade} ano(s).')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
