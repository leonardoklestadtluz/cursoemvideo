"""
Desenvolva um programa que leia o PRIMEIRO NÚMERO de uma PA (progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 21)
print('PROGRESSÃO ARITMETICA')
print('=' * 21)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
  print(f'{c} ', end='-> ')
print('ACABOU')
