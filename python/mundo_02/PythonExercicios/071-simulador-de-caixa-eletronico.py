"""

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa
 vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possuí cédulas de:
R$ 200,00
R$ 100,00
R$ 50,00
R$ 20,00
R$ 10.00
R$ 5,00
R$ 1,00

"""
print('=' * 20)
print('{:^20}'.format('BANCO C&V'))
print('=' * 20)
valorSaque = int(input('Que valor você quer sacar? R$ '))
total = valorSaque
saldo = 2000
ced = 200
totCed = 0
if valorSaque > saldo:
    print(f'[ATENÇÃO] Transação não concluída!! \nSaque R$ {valorSaque} é maior que seu saldo.')
    print(f'Seu saldo atual R$ {saldo}')
else:
    while True:
        if total >= ced:
            total -= ced
            totCed += 1
        else:
            if totCed > 0:
                print(f'Total de {totCed} cédulas de R$ {ced}')
            if ced == 200:
                ced = 100
            elif ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totCed = 0
            if total == 0:
                break
print('=' * 20)
print('Volte sempre ao BANCO C&V! Tenha um bom dia!')

