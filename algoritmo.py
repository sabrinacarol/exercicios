'''Desafio: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento'''


salario = float(input('Digite seu salário: R$ '))
aumento = salario + (salario * 15/100)
print(f' Seu salário era R$ {salario} e o com o aumento ficou R$ {aumento}')
