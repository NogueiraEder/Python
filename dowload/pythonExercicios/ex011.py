a = float(input('Qual a altura da parede em metros ?'))
l = float(input('Qual a Largura da parede em metros?'))

area = a* l
print('a area a ser pintada é:{}m2'.format(area))

litros = area/2
print('Para pintar a area informada vc usará {} litros de tinta!'.format(litros))
