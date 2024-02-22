"""
Faça um programa que leia uma frase pelo teclado e mostre:

    [x] quantas vezes aparece a letra "A"
    [x] em que posição ela aparece a primenira vez
    [] em que posição ela aparece a última vez

"""
frase = input('Escreva uma frase: ').upper()
print('Letra "A" ocorre', frase.count('A'), 'vezes.')
print('Primeira ocorrência da letra "A" no índice:', frase.find('A'))
print('Última ocorrência da letra "A" no índice:', frase.rfind('A'))

