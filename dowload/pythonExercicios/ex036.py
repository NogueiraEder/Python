c = float(input('INFORME O VALOR DO IMOVEL DESEJADO'))
a = int(input('INFORME EM QUANTOS ANOS DESEJA PARCELAR'))
s = float(input('INFORME SEU SALARIO LIQUIDO MENSAL'))
vm = c /a / 12
ps = s * 0.30
print('O VALOR DE R${:.2f},REFERENTE AO IMOVEL PARCELADO EM {}ANOS\ntera uma prestacao mensal no valor de R${:.2f}'.format(c,a,vm))
if ps>vm :
    print('\033[1;32mSeu  financiamento foi Aprovado\033[m!!!')
else:
    print('\033[31m QUE PENA!!,SEU FINANCIAMENTO NAO FOI APROVADO !!! \n \033[1;33;mTENTE FICAR '
          'ABAIXO DE 30% DOS SEUS RENDIMENTOS MENSAIS\033[m!!')



