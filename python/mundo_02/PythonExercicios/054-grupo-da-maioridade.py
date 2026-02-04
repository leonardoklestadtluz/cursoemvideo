"""
Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from  datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    anoNascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.')
print(f'E também tivemos {totalMenor} pessoas menores de idade.')