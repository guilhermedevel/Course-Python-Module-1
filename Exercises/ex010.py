#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ou libras esterlinas ela pode comprar.

#Cotação de moedas realizada em janeiro de 2022

bufunfa = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f} ou £{:.2f}'.format(bufunfa,
                                                               bufunfa/5.39, bufunfa/7.24))
