"""
Faça um programa que leia uma frase pelo teclado e mostre:

    [x] quantas vezes aparece a letra "A"
    [x] em que posição ela aparece a primenira vez
    [] em que posição ela aparece a última vez

"""
frase = str(input('Escreva uma frase: ')).upper().strip()
print('Letra "A" ocorre', frase.count('A'), 'vez(es).')
print('Primeira ocorrência da letra "A" no índice:', frase.find('A') + 1)
print('Última ocorrência da letra "A" no índice:', frase.rfind('A') + 1)

