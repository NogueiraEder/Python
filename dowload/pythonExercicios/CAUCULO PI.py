def parapi(n):
    soma=0
    for i in range(n):
        termo=(-1) ** i/(2*i +1)
        soma+=termo
    return soma *4


n=int(input('Didite o numero de cauculos para pi'))
pi=parapi(n)
print(f'valor de pi = {pi}')