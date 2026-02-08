"""
Faça um programa que leia o PESO de CINCO PESSOAS.
No final, mostre qual foi o MAIOR e o MENOR peso lidos.
"""
pesoMaior = 0
pesoMenor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'O maior peso lido foi de {pesoMaior}Kg.')
print(f'O menor peso lido foi de {pesoMenor}Kg.')
