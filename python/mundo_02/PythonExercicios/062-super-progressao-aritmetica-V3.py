"""
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.

"""
print('=' * 15)
print('GERADOR DE P.A. V2')
print('=' * 15)
primeiro = int(input('1º termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} >>> ', end='')
    termo += razao
    cont += 1
print('PAUSA')