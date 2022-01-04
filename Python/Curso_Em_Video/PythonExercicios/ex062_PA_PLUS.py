primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos: '))
print('Progressão finalizada com {} termos mostrados'.format(total))
