s=0
cont=0
for n in range(1,501,2):
    if n % 3==0:
        s=s+n
        cont=cont+1
print(s)
print(cont)