#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'azul': '\033[34m',
         'magenta': '\033[35m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
num = randint(0, 5)
print('{}-={}'.format(cores['amarelo'], cores['limpa'])*40)
print('{}Olá humano, vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores['azul'], cores['limpa']))
print('{}-={}'.format(cores['amarelo'], cores['limpa'])*40)
palpite = int(input('Em que número eu pensei? '))
print('{}PROCESSANDO...{}'.format(cores['magenta'], cores['limpa']))
sleep(2)
if palpite == num:
    print('{}PARABÉNS! Você conseguiu me vencer!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}{}!'.format(cores['vermelho'], num, palpite, cores['limpa']))
