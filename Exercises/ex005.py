#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na
# tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número qualquer: '))
print('O número sucessor a {} é {}'.format(n1, n1+1))
print('O número antecessor a {} é {}'.format(n1, n1-1))
