#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.

n1 = int(input('Digite um valor qualquer: '))
#solução alternativa:
#dobro = n1 * 2
#triplo = n1 * 3
#raiz = n1**(1/2)
print('O dobro de {} é {}\no triplo de {} é {} \ne a raiz quadrada de {} é {:.2f}'
      .format(n1, (n1*2), n1, (n1*3), n1, pow(n1, (1/2))))
