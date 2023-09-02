

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
while True:
    n = int(input('digite um numero entre 0 e 20 :'))
    while n not in range(0, 21):
        n = int(input('tente novamente.digite um numero entre 0 e 20 :'))
    print(f'vc digitou: {numeros[n]}')
    v=' '
    while v not in'SN':
        v=str(input('Deseja continuar[S/N]')).strip().upper()[0]
    if v=='N':
        break