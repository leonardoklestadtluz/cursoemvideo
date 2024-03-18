"""

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
print('*_*' * 7)
print('Maior e Menor Valores')
print('*_*' * 7)

numero1 = int(input('\nDigite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
numero3 = int(input('Digite o 3º número: '))

menor = numero1
maior = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero1:
    menor = numero3

if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero2 > numero1:
    maior = numero3

print(f'O menor valor digitado foi: {menor}.')
print(f'O maior valor digitado foi: {maior}.')




