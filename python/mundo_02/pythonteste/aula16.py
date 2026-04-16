# TUPLAS SÃO IMUTÁVEIS
pessoa = ('Leonardo', 41, 'M', 82.56)
print(pessoa)
del(pessoa) # deleta a tupla inteira



"""
a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
e = c + d
print(f'Tupla C = {c} | Tupla D = {d} | Tupla E = {e}')
print(f'Tamanho da tupla E = {len(e)} elementos')
print(f'O número {e[1]}, ocorreu {e.count(5)} vezes')
print(f'Posição do número {e[4]} é o índice {e.index(8)}')


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# lanche[1] = 'água' # -> -> -> IMUTÁVEL
print(sorted(lanche))


for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}', end=',\n')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('¨¨¨¨' * 6)
print('PUXA!!! Comi muito ;)')


print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3]) # ignora o último elemento
print(lanche[2:])
print(lanche[:2]) # ignora o elemento de índice 2
print(lanche[-2:])
"""

