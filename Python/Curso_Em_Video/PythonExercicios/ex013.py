# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15% de aumento

salario = float(input('Digite seu salário atual: '))
novo = salario + (salario * 0.15)
print('Seu novo salário com 15% de aumento é igual a {:.2f} reais'.format(novo))
