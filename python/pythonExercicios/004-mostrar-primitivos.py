#004 Faça um programa que leia algo pelo teclado ee mostre na tela o seu tipo primitivo e todas as infomrmações possíveis sobre ele.
algo = input('Digite algo: ')
print(f'O tipo primiivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')

