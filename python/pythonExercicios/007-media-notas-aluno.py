#007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('\n***** MÉDIA DE NOTAS *****\n')

nome = input('Escreva seu nome: ')
print(f'\nBem-vindo ao NoTaS, {nome}\n')
nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))
media = (nota1 + nota2) / 2
print(f'\n{nome}, sua nota média foi de: {media}')


