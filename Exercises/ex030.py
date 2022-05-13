#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

cores = {'magenta': '\033[35m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'limpa': '\033[m'}
num = int(input('{}Me diga um número qualquer:{} '.format(cores['magenta'], cores['limpa'])))
resultado = num % 2
if resultado == 0:
    print('O número {} é {}PAR{}'.format(num, cores['azul'], cores['limpa']))
else:
    print('O número {} é {}ÍMPAR{}'.format(num, cores['vermelho'], cores['limpa']))