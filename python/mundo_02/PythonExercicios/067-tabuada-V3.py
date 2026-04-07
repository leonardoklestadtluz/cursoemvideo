"""

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""
print('*' * 15)
print('*** TABUADA ***')
print('Digite qualquer valor negativo para encerrar.')
print('*' * 15)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('=' * 20)
        break
    else:
        print('-' * 20)
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
        print('-' * 20)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')
