"""
    Desenvolva um programa que leias duas notas
    de um aluno, calcule e mostre a sua média.
"""
nome = input('Informe o nome do aluno: ')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
print(f'Olá {nome}!')
print(f'A média entre as notas {nota1:,.2f} e {nota2:,.2f} é igual a {media:,.2f}')
