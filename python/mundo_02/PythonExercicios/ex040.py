"""

Crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0:
    REPROVADO

- média entre 5.9 e 6.9:
    RECUPERAÇÃO

- Média 7.0 ou superior:
    APROVADO
"""
print('$' * 20)
print('ÀQUELE CLÁSSICO DA MÉDIA')
print('$' * 20)
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
mediaAluno = (nota1 + nota2) / 2
if mediaAluno < 5.0:
    print('REPROVADO')
elif mediaAluno >= 5.9 and mediaAluno < 6.9:
    print('RECUPERAÇÃO')
elif mediaAluno >= 7.0:
    print('APROVADO')
print(f'\nMédia atingida pelo aluno: {mediaAluno}')

