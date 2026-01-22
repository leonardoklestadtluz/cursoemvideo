"""
    Crie um algoritmo que leia um número e
    mostre o seu dobro, triplo e raíz quadrada.
"""
numero = int(input('Digite um núemro = '))
dobro = numero * 2
triplo = numero * 3
# raizQuadrada = numero ** (1/2)
raizQuadrada = pow(numero, (1/2))

print(f'Esse é o dobro: {dobro} do número {numero}.')
print(f'Esse é o triplo: {triplo} do número {numero}.')
print(f'Essa é a raíz quadrada: {raizQuadrada:,.2f} do número {numero}.')
