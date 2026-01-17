"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles escrevendo o nome escolhido.
"""
from random import choice
aluno01 = input('Escreva o nome do 1º aluno(a): ')
aluno02 = input('Escreva o nome do 2º aluno(a): ')
aluno03 = input('Escreva o nome do 3º aluno(a): ')
aluno04 = input('Escreva o nome do 4º aluno(a): ')

alunos = [aluno01, aluno02, aluno03, aluno04]
alunoSorteado = (choice(alunos))

print(f'\nE o aluno(a) sorteado(a) foi: {alunoSorteado}')


