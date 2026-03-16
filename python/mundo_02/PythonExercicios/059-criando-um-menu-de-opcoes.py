from time import sleep
"""
Crie um programa que leia dois valores e mostre um menu na tela.

    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""
primeiroValor = int(input('Qual 1º valor? '))
segundoValor = int(input('Qual 2º valor? '))
adicao = primeiroValor + segundoValor
mulltiplicacao = primeiroValor * segundoValor
opcao = 0
while opcao != 5:
    print('''
        == Escolha uma das opções a seguir ==\n
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiroValor + segundoValor
        print(f'A soma entre {primeiroValor} + {segundoValor} é {soma}')
    elif opcao == 2:
        multiplicacao = primeiroValor * segundoValor
        print(f'A multiplicação entre {primeiroValor} x {segundoValor} = {multiplicacao}')
    elif opcao == 3:
        if primeiroValor > segundoValor:
            maior = primeiroValor
            print(f'1º valor: {primeiroValor} é maior')
        else:
            maior = segundoValor
            print(f'Segundo valor: {segundoValor} é maior')
    elif opcao == 4:
        print('Informe os valores novos')
        primeiroValor = int(input('Qual 1º valor? '))
        segundoValor = int(input('Qual 2º valor? '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
    sleep(3)
print('Fim do programa. Volte sempre!')
