#print('Hello World')
#print('\033[1;31;43mHello, world!')
#print('\033[1;31;43mHello, world!\033[m')
#print('\033[4;30;45mHello, wolrd!\033')
#print('\033[7;30mOlá, mundo!\033[m')
#print('\033[7;33;44mOlá, mundo!\033[m')

#a = 3
#b = 5
#print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Leonardo'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoBranco':'\033[7:30m'
}
print(f'Olá! Muito prazer em te conhecer, {cores["amarelo"]}{nome}{cores["limpa"]}!!!')



