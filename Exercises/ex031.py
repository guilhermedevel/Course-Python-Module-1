#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

cores = {'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
distancia = float(input('{}Qual a distância da sua viagem?{} '. format(cores['ciano'], cores['limpa'])))
print('Você está prestes a iniciar uma viagem de {}{:.2f}Km{}'.format(cores['amarelo'], distancia, cores['limpa']))
price = distancia *0.5 if distancia <= 200 else distancia * 0.45
print('O preço de sua viagem será de {}R${:.2f}{}'.format(cores['verde'], price, cores['limpa']))
