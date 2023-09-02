print('\U0001F83A'*40)
print('  Encontre o Descimo Termo da PA')
print('\U0001F83A'*40)
n1=int(input('Informe o primeiro numero:'))
r= int(input('Informe a razão:'))
print('Os termos da P.A Sao:' )
termo=n1
cont=1
cc=10
total=0

while cc!=0:
    total = total + cc
    while cont<total:
        cont+=1
        termo+=r
        print(n1, end=" \U0001F83A ")

    print('digite 0 para encerrar o programa ou')
    cc = int(input('informe mais quantos termos vc quer ver alem dos 10'))
print('fim')