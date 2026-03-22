"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão aritética usando a estrutura while.

"""
print('=' * 15)
print('GERADOR DE P.A.')
print('=' * 15)
primeiro = int(input('1º termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} >>> ', end='')
    termo += razao
    cont += 1
print('FIM')