dia = float(input('Por quantos dias você alugou o carro ?'))
km = float(input('Qual foi a km total rodado? '))
valor = (dia * 60) + (km * 0.15)
print('O custo total do aluguel do carro foi de {}R$.'.format(valor))