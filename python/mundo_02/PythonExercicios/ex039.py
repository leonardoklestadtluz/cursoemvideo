"""

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- se ele ainda vai se alistar no serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo
"""
print('-+' * 10)
print('ALISTAMENTO MILITAR')
print('-+' * 10)
anoNascimento = int(input('Em que ano você nasceu? '))
anoAtual = 2024
idadeMilitar = anoAtual - anoNascimento
if idadeMilitar <= 18:
    print('Ele(a) ainda vai se alistar no serviço militar.\n')
elif idadeMilitar == 18:
    print('É a hora de se alistar.')
else:
    print('Já passou do tempo de alistamento.')






