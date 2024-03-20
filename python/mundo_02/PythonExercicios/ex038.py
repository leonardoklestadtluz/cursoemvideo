"""
Escreva um program que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

- o primeiro valor é maior
- o segundo valor é maior
- não existe número maior e os dois são iguais
"""
print('-+' * 10)
print('COMPARANDO NÚMEROS')
print('-+' * 10)
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
if num1 > num2:
    print(f'\nO primeiro valor digitado {num1} é maior.')
elif num2 > num1:
    print(f'O segundo valor digitado {num2}, é maior.')
else:
    print(f'Não existe número maior e os dois são iguais, {num1} = {num2}.')
