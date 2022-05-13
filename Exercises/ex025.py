#Exercício Python 025: Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Qual o seu nome completo? ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in name))
