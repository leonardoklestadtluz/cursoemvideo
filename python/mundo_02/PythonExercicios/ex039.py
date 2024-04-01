from datetime import date
"""
Faça um programa que leia o ano de nascimento e o sexo 
de um jovem e informe, de acordo com sua idade:

- se ele ainda vai se alistar no serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo
"""
print('=====' * 5)
print('** ALISTAMENTO MILITAR **')
print('=====' * 5)
anoAtual = date.today().year
sexo = str(input('\nInforme seu sexo, M ou F? '))
if sexo == 'F' or sexo == 'f':
    print(f'\nO serviço militar não é obrigatório para mulheres.')
else:
    anoNascimento = int(input('Qual ano de nascimento? '))
    idadeAlistamento = 18
    idade = anoAtual - anoNascimento
    tempoFaltante = idadeAlistamento - idade
    tempoExcedido = idade - idadeAlistamento
    if idade < 18:
        print(f'Você tem {idade} anos. Ainda faltam {tempoFaltante} anos para seu alistamento.')
    elif idade == 18:
        print(f'Você tem {idade}, anos. Aliste-se IMEDIATAMENTE!')
    elif idade > 18:
        print(f'[[ ATENÇÃO ]] Você tem {idade} anos. Já se passaram {tempoExcedido} anos de seu alistamento!\n'
              f'Compareça a uma base militar, RÁPIDO!')
