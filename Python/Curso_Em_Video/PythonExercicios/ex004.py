# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('È um número? ', a.isnumeric())

