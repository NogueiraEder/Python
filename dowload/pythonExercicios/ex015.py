d = int(input('quatos dias pretende ficar com o carro?'))
km = int(input('quantos km foram percorridos?'))

print('o valor final tendo ficado com o veiculo {}dias e rodado {}km é de R${:.2f}.'.format(d, km,(d*60)+(km*0.15)))