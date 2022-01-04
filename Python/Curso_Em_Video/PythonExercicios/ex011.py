# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
litros = area / 2
print('A área dessa parede é igula a {}\n A quantidade de tinta necessária para pintar essa parede é {} litros.'.format(area, litros))
