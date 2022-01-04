# Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.

num = int(input('Digite um valor: '))
a = num * 2
b = num * 3
# c = num ** 2
# c = num ** (1/2)
c = pow(num, (1/2))
print('O dobro de {} é igual a {}. Seu triplo é igual a {}, e sua raiz quadrada é igual a {:.2f}'.format(num, a, b, c))
