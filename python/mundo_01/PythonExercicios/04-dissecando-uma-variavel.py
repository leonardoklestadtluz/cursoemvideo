"""
    Faça um programa que leia algo pelo teclado e mostre
    na tela o seu tipo primitivo e todas as informações
    possíveis sobre ele
"""

algo = input('Digite algo: ')
print(f'O tipo primitivo é da classe {type(algo)}')
print(f'Alfanumérico, True ou False? {algo.isalnum()}')
print(f'Alfabético, True ou False? {algo.isalpha()}')
print(f'Está na tabela ASCII? {algo.isascii()}')
print(f'É um dígito? {algo.isdigit()}')
print(f'Letras minúsculas? {algo.islower()}')
print(f'É decimal? {algo.isdecimal()}')
print(f'ID válido no Python? {algo.isidentifier()}')
print(f'É numérico? {algo.isnumeric()}')
print(f'Somente espaço(s) em branco? {algo.isspace()}')
print(f'Letras maiúsculas? {algo.isupper()}')
print(f'Pode ser impressa em tela? {algo.isprintable()}')
print(f'Está capitalizado? {algo.istitle()}')
