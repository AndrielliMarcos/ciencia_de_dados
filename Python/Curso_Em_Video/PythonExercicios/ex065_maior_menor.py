x = 'S'
cont = soma = maior = menor = 0
while x != 'N':
    if x == 'S':
        num = int(input('Digite um número: '))
        cont += 1
        soma += num
        if cont == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    x = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = soma / cont
print('A média entre os valores digitados foi {:.1f}'.format(media))
print('O maior número digitado foi {}. E o menor número digitado foi {}.'.format(maior, menor))
