

print('**'*20)
print('           LOJAS NOGUEIRA')
print('**'*20)


v=float(input('Informe o valor da compra!\n:R$'))
print('--'*20)
print('Escolha a Forma de Pagamento')

p=int(input('[1] para pagamento a vista Dinheiro/cheque:\n'
            '[2] para pagamento a vista no Cartao Credito/Debito:\n'
            '[3] para pagamento parcelado em até 2x:\n'
            '[4] para pagamentos parcelado a parir de 3x:\n=' ))
if p == 1:
   f = v * 0.90
   print('o valor do produto com 10% de desconto é{:.2f}'.format(f))

elif  p == 2:
    f= v * 0.95
    print('o valor final com desconto de 5% é {:.2f}'.format(f))


elif p == 3:
    print('parcelado em até 2x o valor final nao se altera R${}'.format(v))
elif p == 4:
    f = v * 1.20
    print('o valor final é R${:.2f}'.format(f))


