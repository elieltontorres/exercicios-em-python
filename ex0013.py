# Leia salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Informe seu salário R$: '))
aumento = (15/100) * salario
salario = salario + aumento
print('Novo salário R$: {:.2f} '.format(salario))