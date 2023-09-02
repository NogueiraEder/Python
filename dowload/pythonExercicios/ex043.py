print('-='*20)
print('\033[1;32m            CALCULADORA IMC !! \033[m')
print('-='*20)
a = float(input('Informe sua altura em metros\n:'))
p = float(input('Informe seu peso em kg\n:'))
imc = p/(a * a)
print('Seu IMC é :\033[1;34m{:.2f}\033[m'.format(imc))
if imc < 18.5:
    print('-=' * 20)
    print('\033[1;30;41m** ALERTA **\033[m')
    print('-=' * 20)
    print('Vc esta\033[1;31m <<<Abaixo>>\033[m do peso')
elif imc >=18.5 and imc < 25:
    print('seu peso é peso Ideal')
    print('\033[1;32m<<<PARABÉNS>>>\033[m')
elif imc >=25 and imc <30:
    print('vc esta com \033[1;33m<<Sobrepeso>>\033[m')
elif imc >=30 and imc < 40:
    print('vc esta com \033[1;33m<<<OBESIDADE>>>\033[m')
else:
    imc >= 40
    print('-=' * 20)
    print('               \033[1;30;41m *** Alerta ***\033[m')
    print('-=' * 20)


    print('vc esta com \033[1;31m<<<OBESIDADE MÓRBIDA>>>\033[m')


