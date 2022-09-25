#Algoritmo que leia o preço de um produto e mostre o novo preço com 5% de desconto

preco = float(input('Informe o preço do produto R$: ' ))
desconto = (5/100) * preco
precofinal = preco - desconto
print('Preço do produto R$: {:.2f} \n Desconto aplicado de 5% \n Novo preço com o desconto aplicado R$ {:.2f} ' .format(preco, precofinal))