#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('{}Qual é o salário do funcionário?{} R$'.format('\033[7m', '\033[m')))
if salario <= 1250:
    aumento = (salario * 15 / 100) + salario
else:
    aumento = (salario * 10 / 100) + salario
print('Quem ganhava \033[1;31mR${:.2f}\033[m passa a ganhar \033[1;34mR${:.2f}\033[m agora'.format(salario, aumento))
