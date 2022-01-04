# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabakhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista) # embaralhar a lista
print('A ordem de aprsentaçã será: ')
print(lista)
