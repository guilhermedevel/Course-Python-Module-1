#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
if velocidade >=81:
    print('{}MULTADO! Você excedeu o limite permitido que é de 80km/h{}'.format(cores['vermelho'], cores['limpa']))
    multa = (velocidade - 80) * 7
    print('{}Você deve pagar uma multa de{} {}R${:.2f}!{}'.format(cores['vermelho'],cores['limpa'],
                                                                  cores['amarelo'], multa, cores['limpa']))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format(cores['verde'], cores['limpa']))
