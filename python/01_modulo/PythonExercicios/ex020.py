"""

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

aluno01 = input('Nome do 1º aluno(a): ')
aluno02 = input('Nome do 2º aluno(a): ')
aluno03 = input('Nome do 3º aluno(a): ')
aluno04 = input('Nome do 4º aluno(a): ')
listaApresentacao = [aluno01, aluno02, aluno03, aluno04]
shuffle(listaApresentacao)
print(f'Esta é a ordem da apresentação: {listaApresentacao}')
