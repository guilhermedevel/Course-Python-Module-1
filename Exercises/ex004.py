#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

v = input('Digite o que vier a sua mente pequeno gafanhoto e te direi o que és: ')
print('O tipo primitivo dessa entrada é: ', type(v))
print('É uma palavra? ', v.isalpha())
print('É um número? ', v.isnumeric())
print('É alfanumérico? ', v.isalnum())
print('Está minúsculo? ', v.islower())
print('Está maiúsculo? ', v.isupper())
print('Está capitalizado? ', v.istitle())
print('Só tem espaços? ', v.isspace())
