n = int(input('escreva um numero de 0 a 9999!').strip())
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m =n // 1000 % 10
print( ' Unidade:{}'.format(u),'\n Dezena {}'.format(d),'\n Centena {}'.format(c),'\n Milhar {}'.format(m) )
