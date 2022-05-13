#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

cores = {'magenta': '\033[35m',
         'limpa': '\033[m',
         'vermelho': '\033[97;41m',
         'azul': '\033[97;44m'}
from datetime import date
ano = int(input('{}Que ano deseja analisar?{} Coloque \033[33m0\033[m para analisar o \033[4;35mano atual\033[m: '.format(cores['magenta'],
                                                                                            cores['limpa'])))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de \033[33m{}\033[m {}é BISSEXTO{}'.format(ano, cores['azul'], cores['limpa']))
else:
    print('O ano de \033[33m{}\033[m {}NÃO é BISSEXTO{}'.format(ano, cores['vermelho'], cores['limpa']))
