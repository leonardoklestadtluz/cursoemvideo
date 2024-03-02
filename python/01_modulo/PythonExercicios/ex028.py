"""
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
from random import randint
from time import sleep

print('-=-' * 20)
print('OLÁ! Digite um número entre 0 e 5!')
print('-=-' * 20, '\n')

numeroAleatorio = randint(0, 5)
numeroDigitado = int(input('Qual número estou pensando? '))
print('PROCESSANDO...')
sleep(3)
mensagemErro = '#### ATENÇÃO, digite um número entre 0 e 5! #####'

if numeroDigitado > 5:
    print(mensagemErro)

if numeroDigitado < 0:
    print(mensagemErro)

if numeroAleatorio == numeroDigitado:
    print(f'PARABÉNS! Você digitou o número: {numeroDigitado} ACERTOU!!!')
else:
    print(f'ERROU! Número digitado por você: {numeroDigitado}.')
    print(f'Eu pensei no número {numeroAleatorio}.')
