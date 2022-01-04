print('''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
''')
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
tot = 0
while tot <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    tot += 1
print('FIM')
