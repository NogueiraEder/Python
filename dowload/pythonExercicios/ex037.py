print('=*='* 20)
print('             \033[1;32m CONVERSOR DE BASES NUMERICAS\033[m!!')
print('=*='* 20)

n = int(input('Escreva o Numero a ser Convertido'))
c = int(input(' Para Convreter Digite:\n[1]para binario\n[2] para octal\n[3] para hexadecimal \n'))
if c== 1:
    conver = bin(n)[2:]
    print(conver)

elif c== 2:
    conver = oct(n)[2:]
    print(conver)


elif c == 3:
    conver = hex(n)[2:]
    print(conver)

else:
    print('\033[1;33mOpção não encontrada tente novamete selecionando um numero ente 1 e 3\033[1m!!!\033[m')
print ( 'O numero {} convertido para a base {} é {}' . format ( n , c , conver))