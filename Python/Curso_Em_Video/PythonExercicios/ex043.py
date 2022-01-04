print('''Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obecidade mórbida
''')
from math import pow
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / pow(altura, 2)

if imc <= 18.5:
    texto = 'ABAIXO DO PESO'
elif 18.5 < imc <= 25.0:
    texto = 'PESO IDEAL'
elif 25.0 < imc <= 30.0:
    texto = 'SOBREPESO'
elif 30.0 < imc <= 40.0:
    texto = 'OBESIDADE'
else:
    texto = 'OBESIDADE MÓRBIDA'
print('Seu IMC é igual a {:.1f}. De acordo com seu imc, seu status é: {}.'.format(imc, texto))



