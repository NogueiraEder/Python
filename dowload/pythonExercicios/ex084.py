
np=list()
inf=list()
cont=cont2=0
maior=0
menor=0

while True:
    s=str(input('digite seu nome'))
    p=int(input(f'Informe seu peso'))
    np.append(s)
    np.append(p)
    inf.append(np[:])
    np.clear()
    cont+=1
    v=str(input('Deseja continuar?[S/N]')).strip().lower()[0]
    if v in 'n':
        break
print(f'vc cadastrou {cont} pessoas')
for p in inf:
    cont2+=1
    if cont2==1:
        maior=p[1]
        menor=p[1]

    else:
        if p[1]>=maior:
            maior=p[1]

        if p[1]<=menor:
            menor=p[1]



print(f'o maior peso foi: {maior}kg peso de: ',end='')
for p in inf:
    if p[1] == maior:
        print(f'[{p[0]}], ',end='')
print()
print(f'o menor peso foi: { menor}kg peso de ',end='')
for p in inf:
    if p[1] == menor:
        print(f'[{p[0]}],',end='')
print()

