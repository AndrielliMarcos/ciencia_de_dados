print('''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SENIOR
Acima: MASTER
''')
from datetime import date
anoNascimento = int(input('Digite o ano e seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade <= 9:
    texto = 'MIRIM'
elif 9 < idade <= 14:
    texto = 'INFANTIL'
elif 14 < idade <= 19:
    texto = 'JÚNIOR'
elif 19 < idade <= 20:
    texto = 'Sênior'
elif idade > 20:
    texto = 'MASTER'
print('Você tem {} anos. Então você pertence a categoria {}.'.format(idade, texto))
