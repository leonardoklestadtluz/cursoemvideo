"""
Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
print('='*20)
print(' VALIDADOR DE DADOS ')
print('='*20)
sexo = str(input('Informe um sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    if sexo == 'M':
        sexo
    else:
        sexo = str(input('Informe um sexo [M/F]: ')).strip().upper()
print(f'Sexo digitado: {sexo}')