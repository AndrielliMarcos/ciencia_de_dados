print('''Faça um programa que leia três números e mostre qual é o maior e qual é o menor''')

a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite um outro número: '))
# Verificando que é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Entre os números digitados o maior é {} e o menor é o {}'.format(maior, menor))
