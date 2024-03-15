nome = str(input('Qual é o seu nome? '))
nomeBonito = 'Leonardo'
if nome == nomeBonito:
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'{nome}, seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')
