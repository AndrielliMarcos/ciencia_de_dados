'''for c in range(1, 10):
    print(c)
print('FIM')'''
# O FOR e o WHILE serve para todas as situações que sabemos o limite
'''c = 0
while c < 10:
    print(c)
    c += 1
print('FIM')'''
# mas quando não sabemos o limite podemos usar somente o WHILE
'''n = 1
while n != 0: # n!=0 é a flag(ponto de parada)
    n = int(input('Digite um valor: '))
print('FIM')'''
r = 'S'
'''while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # para o 0 não entrar na contagem de pares
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

