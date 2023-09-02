from time import sleep
h = int(input('escreva um numero para ver a taboada\n:'))
for n in range(1,11):
    print('{}x{}={}'.format(n,h,n*h))
    sleep(0.4)

print('pratique!!')