"""
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS.

No final do programa, mostre:

    * A MÉDIA DE IDADE do grupo.
    * Qual é o nome do homem MAIS VELHO.
    * Quantas mulheres tem MENOS DE 20 anos.
"""
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
totMulher20 = 0
for pessoa in range(1, 5):
    print(f'\n---- {pessoa}ª PESSOA ----')
    nome = str(input(f'Qual é o nome {pessoa}ª pessoa? '))
    idade = int(input(f'Qual a idade da {pessoa}ª pessoa? '))
    sexo = str(input(f'Qual o seu sexo da {pessoa}ª pessoa [M/F]? ')).strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaIdade = somaIdade / 4
print(f'\nA média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeMaisVelho}.')
print(f'Ao todo são {totMulher20} mulheres com menos de 20 anos.')








