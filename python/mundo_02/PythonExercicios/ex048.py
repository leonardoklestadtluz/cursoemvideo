"""
Faça um programa que calcula a SOMA entre todos os NÚMEROS ÍMPARES  que são MÚLTIPLOS DE TRÊS e que se encontram
no intervalo de 1 até 500.
"""
for numero in range(1, 500 + 1):
  if numero % 2 != 0:
    print(numero)
