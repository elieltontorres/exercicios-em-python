#Leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis

n = (input('Informe algo: '))
print('O tipo primitivo é:', type(n))
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanúmerico?', n.isalnum())
print('É maiúsculo? ', n.isupper())
print('É minúsculo? ', n.islower())
print('Possui só espaços?', n.isspace())
