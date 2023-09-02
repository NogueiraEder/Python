import math
angulo = int(input('informe o o angulo desejado.'))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tang = math.tan(rad)

print('com o angulo{:-^6.2f} temos o seno: {:-^6.2f} o cosseno: {:-^6.2f} e a tangente: {:-^6.2f} '.format(angulo, seno, cosseno, tang))