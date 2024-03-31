from datetime import date
"""
Faça um programa que leia o ano de nascimento e o sexo 
de um jovem e informe, de acordo com sua idade:

- se ele ainda vai se alistar no serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo
"""
anoAtual = date.today().year
sexo = str(input('Informe seu sexo, M ou F? '))
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

# FALTA DESENVOLVER A CONDIÇÃO DO SEXO FEMININO

if sexo == 'F' or sexo == 'f':
    print(sexo)
else:
    print(f'O serviço militar não é obrigatório para mulheres.')
    opcao = input('Deseja alistar-se, S ou N? ')
    if opcao == 'S' or opcao == 's':
        print('Preencha o formulário com suas informações')
    elif opcao == 'N' or opcao == 'n':
        print('Obrigado por suas respostas.')










# print(f'Ano atual: {anoAtual}')
# print(f'Ano de nascimento: {anoNascimento}')
# print(f'Sexo: {sexo}')



