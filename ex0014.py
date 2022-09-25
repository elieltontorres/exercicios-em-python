#Programa que leia largura e altura da parede em metros, calcula sua área e informa a quantidade de tinta para pintala
largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²' .format(largura, altura, area))
tinta = area/2
print('Para pintar sua parede, você irá precisar de {}l de tinta.'.format(tinta))