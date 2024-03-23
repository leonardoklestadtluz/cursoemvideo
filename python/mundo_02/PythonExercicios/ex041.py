"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade.

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SÊNIOR
- acima: MASTER

"""
print('=-=' * 10)
print('CLASSIFICANDO ATLETAS')
print('=-=' * 10)
anoNascimento = int(input('Em que ano o atleta nasceu? '))
anoAtual = 2024
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Categoria: MIRIM')
elif idade >= 10 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Categoria: JÚNIOR')
else:
    print('Categoria: SÊNIOR')
