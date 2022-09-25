#Operadores aritméticos

n1 = int (input('Informe o valor de n1: '))
n2 = int (input('Informe o valor de n2: '))
soma = n1 + n2
subt = n1 - n2
multip = n1 * n2
div = n1 / n2
divint = n1 // n2
divresto = n1 % n2
pot = n1 ** n2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {}' .format(soma, subt, multip))
print('A divisão vale {}, a divisão inteira vale {}, o resto d divisão é {} e a potência é {}'.format(div, divint, divresto, pot))