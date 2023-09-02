lista = ('CASA', 'BARRACA', 'MESA',
         'BARCO', 'FAROL', 'MARUJO',
         'SEREIA')


for p in lista:
    print(f'\n a palavra {p} tem as vogais :',end=' ')
    for l in p:
        if l in 'AEIOU':
            print(l,end=' ')
