"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler o número pelo teclado(entre 0 e 20) e transformá-lo por extenso
"""
cont = ('zero','um','dois','tres','quatro',
        'cinco','seis','sete','oito',
        'nove','dez','onze','doze',
        'treze','quatorze','quinze','dezesseis',
        'dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('[ERRO] Tente Novamente! ', end='')
print(f'Você digitou o número {cont[num]}.')





