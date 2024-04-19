from time import sleep
# import emoji
"""
Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de
artifício, indo de 10 ATÉ 0, com uma pausa de 1 SEGUNDO entre eles.
"""
print('*&*' * 7)
print('CONTAGEM REGRESSIVA')
print('*&*' * 7)
for c in range(10, 0, -1):
    sleep(1)
    print(f'{c}...')
sleep(1)
print('\n*******************************')
print('*** BOOM!!! BOOM!!! BOOM!!! ***')
print('*******************************')














""" BIBLIOTECA emoji NÃO ESTÁ FUNCIONANDO >>> CORRIGIR!!!

print(emoji.emojize(':candle:', language='alias') * 9)
print('CONTAGEM REGRESSIVA')
print(emoji.emojize(':candle:', language='alias') * 9)
for c in range(10, 0, -1):
    sleep(1)
    print(emoji.emojize(f':ZZZ::ZZZ::ZZZ: {c}', language='alias'))
sleep(1)
print(emoji.emojize(':collision::collision::collision::collision::collision::collision:', language='alias'))
"""