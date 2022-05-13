#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

print('\033[1;35m-=\033[m'*20)
print('\033[1;36mAnalisador de triângulos\033[m')
print('\033[1;35m-=\033[m'*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b+c and b < a+c and c < a+b:
    print('Os segmentos acima \033[4;32mPODEM\033[m formar um triângulo')
else:
    print('Os segmentos acima \033[4;31mNÃO PODEM\033[m formar um triângulo')
