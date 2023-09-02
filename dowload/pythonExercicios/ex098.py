from time import sleep
def contador(i,f,p):
    print(f'cont de {i} ate {f} passo {p}')
    cont = i
    p=abs(p)
    if p==0:
        p=1
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ',flush=True)#para mostrar numero a numero ou tudo junto!!
            cont += p
            sleep(0.2)
        print()
    else:
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.2)
        print()


contador(1,10,1)
contador(10,0,2)
print('INFORME OS VALORES DESEJADOS!!')
print('*-*'*16)
contador(i=int(input('inicio: ')),f=int(input('fim: ')),p=int(input('passo: ')))
print('*-*'*16)
# def per(i,f,p):
#     print(f'cont de {i} ate {f} passo {p}')
#     cont=i
#     if i < f:
#         while cont <= f:
#             print(f'{cont}', end=' ')
#             cont += p
#             sleep(0.3)
#         print()
#     else:
#         while cont >= f:
#             print(f'{cont}', end=' ')
#             cont -= p
#             sleep(0.5)
#         print()
#
#
# per(i=int(input('inicio: ')),f=int(input('fim: ')),p=int(input('passo: ')))
