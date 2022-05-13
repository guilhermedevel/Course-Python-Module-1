#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
print('Se o cateto oposto mede {}cm\nE o cateto adjacente mede {}cm\nA hipotenusa vai medir {:.2f}cm'
      .format(x, y, hypot(x, y)))
