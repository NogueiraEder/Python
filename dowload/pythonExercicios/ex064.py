
n=cont=soma=0

n=int(input('digite um numero[999]-fim'))
while n!=999:
    cont+=1
    soma+=n
    n = int(input('digite um numero[999]-fim'))
print(f'''foram{cont}numeros digitado e a soma entre eles é{soma}''')