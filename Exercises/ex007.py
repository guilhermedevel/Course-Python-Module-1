#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule
# e mostre a sua média.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2)/2
print('Em sua primeira avaliação o aluno tirou a nota {:.1f}\nEm sua segunda '
      'avaliação o aluno tirou a nota {:.1f}\nLogo sua média foi de {:.1f}'.format(n1, n2, m))
