'''
Crie um programa que leia a idade e o sexo de váris pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
Np final, mostre:
Quantas pessoas têm mais de 18 anos
Quantos homens foram cadastrados
Quantas mulheres têm menos de 20 anos
'''
contIdade = contHomens = contMulheres = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MnFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheres += 1
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'NnSs':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contHomens} homens cadastrados.')
print(f'E temos {contMulheres} mulheres com menos de 20 anos.')




