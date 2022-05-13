#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido
# em quilometros, hectometros, decametros, decímetros,  centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
print('A medida de {} metros corresponde a:\n'
      '{} quilometros\n'
      '{} hectometros\n'
      '{} decametros\n'
      '{} decímetros\n'
      '{} centímetros\n'
      '{} milímetros'.format(m, m/1000, m/100, m/10, m*10, m*100, m*1000))
