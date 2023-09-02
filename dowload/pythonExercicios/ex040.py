a = float(input('me diga sua primeira nota\n:'))
b = float(input('me diga sua segunda nota \n:'))
media = (a + b) / 2
if media < 5:
    print('\033[1;31m REPROVADO!!!\033[m')
    print('sua media é :{}'.format(media))
elif media >=5 and media < 7:
    print('voçe esta na recuperaçao')
    print('sua media é :{}'.format(media))
elif media >=7 :
    print("APR0VADO")
    print('sua media é :{}'.format(media))