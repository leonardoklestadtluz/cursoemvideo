"""

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

"""
n = c = s = 0
while True:
    n = int(input('Digite um número inteiro qualquer (999 pra parar): '))
    if n <= 0:
        print(f'[ERRO]: Número {n} é inválido. Fim do programa')
        break
    if n == 999:
        break
    s += n
    c += 1
print(f'\nTotal de números digitados: {c}')
print(f'A soma dos números digitados foi: {s}')

