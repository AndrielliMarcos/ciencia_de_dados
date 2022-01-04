print('''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
''')
sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0] # retirando os espaços e pegando somente a primeira letra do que foi digitado
# while sexo not in 'MmFf':
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
