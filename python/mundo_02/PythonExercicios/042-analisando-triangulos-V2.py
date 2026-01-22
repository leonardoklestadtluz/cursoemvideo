"""

Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print('=-' * 15)
print('ANALISANDO TRIÂNGULO v2.0')
print('=-' * 15)
linha01 = float(input('\nDigite a medida da 1ª linha: '))
linha02 = float(input('Digite a medida da 2ª linha: '))
linha03 = float(input('Digite a medida da 3ª linha: '))
if linha01 < linha02 + linha03 and linha02 < linha01 + linha03 and linha03 < linha01 + linha02:
    print('\nAs linhas acima formam um triagulo ', end='')
    if linha01 == linha02 == linha03:
        print('EQUILATERO')
    elif linha01 != linha02 != linha03 != linha01:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\nAs linhas acima não podem formar um triângulo.')
