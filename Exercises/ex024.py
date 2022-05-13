#Exercício Python 024: Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

City = str(input('Em que cidade você nasceu? ')).strip().capitalize()
print(City[:5] == 'Santo')
