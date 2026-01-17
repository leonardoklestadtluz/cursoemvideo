from random import randint
from time import sleep
from sys import exit
"""
Crie um programa que faça o computador jogar Jokenpô (pedra, papel, tesoura), com você.

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).
"""
print('#_#' * 12)
print('&& GAME: Pedra, Papel, Tesoura &&')
print('#_#' * 12)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
if jogador > 2:
    print('JOGADA INVÁLIDA!')
    exit()
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
