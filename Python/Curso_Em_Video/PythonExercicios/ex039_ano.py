print('''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é hora de se alistar.
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
''')
from datetime import date
print('''Sexo:
[ F ] Feminino
[ M ] Masculino
''')
sexo = str(input('Sexo: ')).strip().upper()
if sexo == 'F':
    print('No Brasil, o alistamento de mulheres não é obrigatório. Você está dispensada!')
elif sexo == 'M':
    nascimento = int(input('Digite o ano de seu nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    print('Você nasceu em: {}. Em {} você terá {} anos.'.format(nascimento, anoAtual, idade))
    if idade < 18:
        tempo = 18 - idade
        print('Falta(m) {} ano(s) para você se alistar no serviço militar.'.format(tempo))
        ano = anoAtual + tempo
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Está na hora de você se alistar ao serviço militar!')
    else:
        tempo = idade - 18
        print('Você deveria ter se alistado há {} ano(s)!'.format(tempo))
        ano = anoAtual - tempo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Digite [ F ] Feminino ou [ M ] Masculino')
