'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo 
que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
'''
dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R$ {pago:.2f}')
