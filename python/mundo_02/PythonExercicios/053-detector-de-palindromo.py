"""
Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
"""

# radar
# o rato roeu a roupa do rei de roma

print('*' * 22)
print('DETECTOR DE PALÍNDROMO')
print('*' * 22)
frasePalavra = str(input('Escreva uma frase ou palavra(s): ')).strip().upper()
palavras = frasePalavra.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso} ')
if inverso == junto:
    print(f'A frase/ palavra {frasePalavra} é um PALÍNDROMO')
else:
    print(f'A frase/ palavra {frasePalavra} não é um PALÍNDROMO')



