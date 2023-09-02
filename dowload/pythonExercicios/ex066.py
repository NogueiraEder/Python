soma = cont = n = 0
while True:
    cont+=1
    soma+=n
    n=int(input(f'type it a nunber or [999] for get out:'))
    if n==999:
        break
print(f'you enter {cont} values and the sum is: {soma}')
