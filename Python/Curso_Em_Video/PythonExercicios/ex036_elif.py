print('''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, abendo que ela não pode exceder 30% do salário ouentão o empréstimo será negado
''')
valorCasa = float(input('Digite o valor da casa que você deseja comprar: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos você pretende pagar o imóvel: '))
print('Valor da casa: {:.2f} \n Valor do salário: {:.2f} \n Em quanto tempo irá pagar: {} anos'.format(valorCasa, salario, anos))
valorMensal = valorCasa / (anos * 12)
porcentagemSalario = salario * 0.30
if valorMensal <= porcentagemSalario:
    print('Parabéns! Seu empréstimo foi aprovado e você poderá comprar seu imóvel e pagará R${:.2f} mensalmente'.format(valorMensal))
else:
    print('Seu empréstimo foi negado!')
