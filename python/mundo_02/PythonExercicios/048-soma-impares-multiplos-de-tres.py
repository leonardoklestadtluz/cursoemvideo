"""
Faça um programa que calcula a SOMA entre todos os NÚMEROS ÍMPARES
que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500.
"""
print('=_=' * 10)
print('SOMA ÍMPARES MÚLTIPLOS DE TRÊS')
print('=_=' * 10)
somaImpar = 0
for numero in range(1, 500):
    if numero % 2 != 0:
        somaImpar += numero
print(f'\nSomatório dos número ímpares = {somaImpar}.')


# FALTA FAZER A CONDIÇÃO PARA OS MÚLTIPLOS DE TRÊS
# numeroFixo = 3
# numeroInteiro += 3
# incremento = numeroInteiro
# resultado = (numeroFixo * numeroInteiro) / numeroInteiro
# print(numeroInteiro)
# print(resultado)

