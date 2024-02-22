"""
Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Exemplo:
    Nome completo: Ana Maria de Souza
    primeiro = Ana
    último = Souza
"""
nomeCompleto = input('Informe seu nome completo: ').capitalize()
print('Primeiro nome =', nomeCompleto.split()[0])
print('Último nome = ', nomeCompleto)


