nome = input('Qual é o seu nome? ')

#alinhamento padrão
print(f'Prazer em te conhecer {nome:20}!')

#alinhamento à esquerda
print(f'Prazer em te conhecer {nome:<20}!')

#alinhamento à direita
print(f'Prazer em te conhecer {nome:>20}!')

#alinhamento ao centro
print(f'Prazer em te conhecer {nome:^20}!')

#alinahmento central com caracteres ao redor
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(
    f'Soma = {s}, '
    f'multiplicação = {m}, '
    f'divisão = {d:.3f}, '
    f'divisão inteira = {di}, '
    f'exponenciação = {e}'
)






























