"""
Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍDROMO, desconsiderando os espaços.
"""
print('=' * 21)
print('DETECTOR DE PALÍNDROMO')
print('=' * 21)
frase = str(input("Digite uma frase/ palavra: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'A frase/ palavra: {frase} É um palíndromo')
else:
    print(f'A frase/ palavra: {frase} NÃO é um palíndromo')
