import random
import time as s


def maior(* num):
    cont = maio = 0
    print('--'*15,end='')
    print('\nEm analise!!')
    for v in num:
        print(v,end=' ')
        s.sleep(0.5)
        if cont == 0:
            maio = v
        else:
            if v > maio:
                maio = v

        cont += 1
    print(f' o maior valor informafo foi {maio}')

maior(2,9,5,1)
maior(7,3,5)
maior(2,15)
maior()



