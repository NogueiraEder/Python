soma = 0
cont = 0
for n in range(1,7):
    num = int(input('escreva o {} valor'.format(n)))
    if num %2==0:
        soma+=num    #soma= soma+num
        cont+=1          #contador = contador + 1
print('A soma dos {} numeros pares é:{}'.format(cont,soma))



     

