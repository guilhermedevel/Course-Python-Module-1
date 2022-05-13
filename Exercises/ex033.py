#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o {}primeiro{} número: '.format('\033[4;36m', '\033[m')))
n2 = int(input('Digite o {}segundo{} número: '.format('\033[4;34m', '\033[m')))
n3 = int(input('Digite o {}terceiro{} número: '.format('\033[4;32m', '\033[m')))

# Verificando quem é o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O {}menor{} valor digitado foi \033[4;31m{}\033[m'.format('\033[30;41m', '\033[m', menor))
print('O {}maior{} valor digitado foi \033[4;33m{}\033[m'.format('\033[30;43m', '\033[m', maior))
