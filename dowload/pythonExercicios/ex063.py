

print('*'*20)
print('sequência de fibonacci')
print('*'*20)

q = int(input('informequantos numeros da sequencia vc quer ver :'))
t1=0
t2=1
print('{} \U0001F83A {}'.format(t1,t2),end='')
cont=3
while  cont<=q:
    t3=t1+t2
    print(' \U0001F83A {}'.format(t3),end='')
    cont+=1
    t1=t2
    t2=t3
print('fim')
# 1  1  2    3     5
#   t1  t2   t3    |
#       t1   t2   [t3]   t1=t2 _ t2=t3
# vamos traspor o lugar dos termos para encontrar o proximo da seguencia
# somando os antecedentes
# [t3=t1+t2]
# e faremos isso enguanto  contaguem for menor igual ao valor digitado