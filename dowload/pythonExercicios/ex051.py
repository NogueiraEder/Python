print('\U0001F83A'*40)
print('  Encontre o Descimo Termo da PA')
print('\U0001F83A'*40)
n1=int(input('Informe o primeiro numero:'))
r= int(input('Informe a razão:'))
f= n1 +(11-1)* r # formula para encontrar o termo da pa

for d in range(n1,f,r):
    print(d,end=' \U0001F83A ')



