cont=0
n = int(input('Informe um numero'))
for c in range(1,n+1):
    #print(c,end=' ')
    if n%c==0:
        print('\033[1;33m',end=' ')
        cont+=1
    else:
        print('\033[m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mo valor é divisivel por \033[33m{} \033[m numero'.format(cont))
if cont==2:
    print('\033[32mé um numero primo\033[m')
else:
    print('\033[31mnao é primo\033[m')