print('''Faça um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez
''')

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" apareceu {} vezes nesta frase.'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posiçõe: {}'.format(frase.upper().find('A') + 1))
print('A letra "A" aparece pela úlima vez na posiçãp: {}'.format(frase.upper().rfind('A') + 1))


