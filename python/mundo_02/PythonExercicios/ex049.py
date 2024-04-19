"""
Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher,só que agora utilizando o LAÇO FOR.
"""
print('=' * 13)
print('TABUADA v.2.0')
print('=' * 13)
numero = int(input('Tabuada do número? '))
print('=' * 27)
print(f'*** Tabuada do Número {numero} ***')
for mult in range(0, 10 + 1):
    resultado = numero * mult
    print(f'{numero} x {mult} = {resultado}')
print('=' * 27)

