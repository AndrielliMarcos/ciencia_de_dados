print('''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isóceles: dois lados iguais
Escaleno: todos os lados diferentes
''')
r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    if r1 == r2 == r3:
        texto = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        texto = 'ISÓSCELES'
    elif r1 != r2 != r3 != r1:
        texto = 'ESCALENO'
    print('Os seguimentos acima podem forma um triângulo do tipo {}.'.format(texto))
else:
    print('Os segmentos acima não podem formar um triângulo')
