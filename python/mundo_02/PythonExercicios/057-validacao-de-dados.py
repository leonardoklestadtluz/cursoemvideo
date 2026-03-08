"""
Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
print('='*20)
print(' VALIDADOR DE DADOS ')
print('='*20)
sexo = str(input('Informe um sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')