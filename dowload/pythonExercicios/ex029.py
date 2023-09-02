v = int(input('informe a velocidade em que o veiculo passou pelo radar:'))
if v <= 80:
    print('parabens continue dirigindo com cuidado e tenha um bom dia!!!')
else:
    print('voçe Foi Multado!!!')
    print('sua multa e de R${:.2f}'.format((v-80)*7))
