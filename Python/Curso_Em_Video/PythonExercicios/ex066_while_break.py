'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
o flag)
'''
cont = soma = 0
while True:
    num = int(input('Digite um valor qualquer ou 999 para parar o programa: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números. A soma entre ele é igual a {soma}.')
print('------ FIM DO PROGRAMA ------')
