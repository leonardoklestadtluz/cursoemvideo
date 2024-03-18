nome = 'Leonardo'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoEbranco': '\033[7;38m'
}
print(f'Olá! Muito prazerem te conehcer, meu nome é {cores['pretoEbranco']}{nome}{cores['limpa']}.')
# a = 3
# b = 5
# print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m.')
# print('\033[7;33;44mHello, world!\033[m')
