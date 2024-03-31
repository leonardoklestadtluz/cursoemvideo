"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

1 - à vista dinheiro/ cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço normal
4 -  3x ou mais no cartão: 20% de juros
"""
precoInformado = float(input('Informe o preço do produto R$ '))
acrecimoJuros = (20 * precoInformado) / 100
condicao1 = precoInformado - ((10 * precoInformado) / 100)
condicao2 = precoInformado - ((5 * precoInformado) / 100)
condicao3 = (precoInformado / 2) * 2
condicao4 = ((precoInformado / 3) + acrecimoJuros) + precoInformado
print('\n**** Condição de Pagamento ****\n'
      '1 - à vista dinheiro/ cheque: 10% de desconto\n'
      '2 - à vista no cartão: 5% de desconto\n'
      '3 - em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros\n')
condicaoPagamento = int(input('Escolha a Condição do Pagamento: '))
if condicaoPagamento == 1:
    print(f'\nValor total de sua compra ficou em R$ {condicao1:.2f}')
elif condicaoPagamento == 2:
    print(f'\nValor total de sua compra ficou em R$ {condicao2:.2f}')
elif condicaoPagamento == 3:
    print(f'\nValor total de sua compra ficou em R$ {condicao3:.2f}')
elif condicaoPagamento == 4:
    print(f'\nValor total de sua compra ficou em R$ {condicao4:.2f}')
else:
    print(f'\nCondição de pagamento: {condicaoPagamento} inválida! '
          f'\nEscolha uma das condições disponíveis.')
