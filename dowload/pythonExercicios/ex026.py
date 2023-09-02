f = str(input('digite sua frase!!')).strip().lower()
print('A letra a apareçe {} vezes'.format(f.count('a')))
print('aparece primeiro na posicao {}'.format(f.find('a')))
print('aparece por ultimo na posicao: {}'.format(f.rfind('a')))