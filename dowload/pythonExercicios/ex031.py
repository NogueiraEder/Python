d = int(input('informe a distancia da viagem em km'))
if d < 200:
    print('o valor da viagem é de R${:.2f}'.format(d * 0.50))
else:
    print('ovalor da viagem é de: R${:.2f}'.format(d * 0.45))