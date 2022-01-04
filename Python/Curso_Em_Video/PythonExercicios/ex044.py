print(''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
''')
valorProduto = float(input('Digite o valor do produto: R$'))
print('Formas de pagamento:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Escolha a forma de pagamento: '))
if pagamento == 1:
    valorFinal = valorProduto - (valorProduto * 0.10)
elif pagamento == 2:
    valorFinal = valorProduto - (valorProduto * 0.05)
elif pagamento == 3:
    valorFinal = valorProduto
elif pagamento == 4:
    valorFinal = valorProduto + (valorProduto * 0.20)
else:
    print('Forma de pagamento inválida! Consulte as formas de pagamento existentes.')
print('Você irá pagar R${:.2f} pelo prduto adquirido.'.format(valorFinal))

