#Aluguel de carros

km_percorrido = float(input('Informe a quantidade de KM percorridos pelo carro: '))
diasAluguel = int(input('Informe a quantidade de dias do aluguel do carro: '))

preco_aluguel = (diasAluguel * 60) + (km_percorrido * 0.15)
print('Total a pagar RS: {:.2f}' .format(preco_aluguel))