# cont = 0
# while True:
#     v = int(input('quer ver a taboada de qual valor? :  '))
#     print('---'*10)
#     while cont !=10:
#         cont += 1
#         mut=v*cont
#         print(f'{v}x{cont}={mut}')
#     print('---' * 10)
#     if v <0:
#         break
#     fazedo com for é ate mais simples

while True:
    v = int(input('quer ver a taboada de qual valor? :  '))
    print('---' * 10)
    for cont in range(1,11):
        mut = v * cont
        print(f'{v}x{cont}={mut}')
    print('---' * 10)
    if v < 0:
        break

