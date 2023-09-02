from calendar import isleap
from datetime import date

n =int(input('informe o ano para verificar se é bissexto!!! Informe "0" para o ano Atual'))
if n==0:
   n = date.today().year
print('calculando o ano', n)
if isleap(n):
    print('É BISSEXTO')
else:
    print('NÃO É BISSEXTO')

##from datetime import date
#ano = int(imput('Que ano quer analizar? digite 0 para analizar o ano atual)
#if ano==0:
 #   ano= date.today().year
#if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
#     Print('0 ano {} é bissexto'.format(ano))
#else:
  #  print('0 ano {} nao é bissexto'.format(ano))
#
#
#
#