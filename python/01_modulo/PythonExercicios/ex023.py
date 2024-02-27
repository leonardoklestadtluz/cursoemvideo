"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Exemplo:
    Digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1

isso >>> [0:4] <<< no final da linha da declaração da variável numero
permite a digitar mais que quatro números, mas considera somente
os 4 primeiros
"""
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Analisando o número: {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Milhar: {centena}')
print(f'Centena: {milhar}')

