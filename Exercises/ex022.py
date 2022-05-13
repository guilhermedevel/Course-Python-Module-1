#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
split = nome.split()
join = ''.join(split)
print('Analisando seu nome...\nSeu nome em maiúsculas é {}\n'
      'Seu nome em minúsculas é {}'.format(nome.upper(), nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(join)))

#A linha 14 é uma solução alternativa para a linha 11
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome é {} e ele tem {} letras'.format(split[0], len(split[0])))

#A linha 19 é uma solução alternativa para a linha 16
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
