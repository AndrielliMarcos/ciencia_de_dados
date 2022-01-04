print('''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão''')
num = int(input('Digite um número inteiro qualquer: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')
base = int(input('Qual conversão você deseja? '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # vai começar a contar a partir do indice 2
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Digite 1, 2 ou 3!')



