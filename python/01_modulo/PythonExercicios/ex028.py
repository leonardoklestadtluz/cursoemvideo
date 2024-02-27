"""
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
import random

numeroDigitado = print('Qual número estou pensando?')

numeroAleatorio = random.randint(0, 5)


if numeroAleatorio == numeroDigitado:
    print(f'PARABÉNS! Você digitou o número: {numeroDigitado} acertou.')
else:
    print(f'ERROU! Número digitado por você: {numeroDigitado}.')
    print(f'Eu pensei no número {numeroAleatorio}.')
