#Programa que leia o valor em metros e mostre convertido em centimetros e milimetros

n1 = float (input('Informe o valor em metros: '))
cm = n1 * 100
mm = n1 * 1000
print(' Valor informado em metros: {} \n Resultado convertido para centimetros {} e milimetros {}' .format(n1, cm, mm))


