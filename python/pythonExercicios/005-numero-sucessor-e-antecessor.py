#005 Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
print('\n***** NÚMEROS ANTECESSOR E SUCESSOR *****\n')

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'Antecessor {antecessor} | Número {numero} | Sucessor {sucessor}')
