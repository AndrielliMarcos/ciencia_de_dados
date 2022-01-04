print('''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999
No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag
''')
num = 0
cont = soma = 0
while num != 999:
    num = int(input('Digite um valor qualquer ou 999 para sair: '))
    if num != 999:
        cont += 1
        soma += num
print('Foram digitados {} números. A soma entre eles é igual a {}'.format(cont, soma))


