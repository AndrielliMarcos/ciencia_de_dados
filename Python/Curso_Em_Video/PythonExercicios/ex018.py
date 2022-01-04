# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math
angulo = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f} \n COSSENO de {:.2f} \n e TANGENTE de {:.2f}'.format(angulo, seno, cos, tan))
