#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l*a
print('Sua parede tem a dimensão de {}mx{}m e sua área é de {}m²'.format(l, a, ar))
print('Para pintar essa parede você precisará de {}l de tinta'.format(ar/2))
