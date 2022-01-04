print('''
Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.
ex.:
Apos a sopa.
A sacada da casa.
A torre da derrota
''')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # separa por palavras
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # ler junto de trás para frente
    inverso += junto[letra] # ler a palavra junto no indice letra
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

