from datetime import date
n = int(input('informe seu  ano de nascimento: '))
a =date.today().year
idade = a - n
print('quem nasceu em {} completa {} anos em {}'.format(n,idade,a))

genero = int(input('Qual seu Genero de Nascimento'
                  ' \n[1] masculino\n[2]feminino \n:'))

if idade == 18 and genero == 1:
    print('hora de se alistar')

elif idade < 18 and genero == 1:
    faltam =18 - idade
    ano= a + faltam
    print('faltam {} anos para seu alistamento'.format(faltam))
    print('seu alistamento sera em:{}'.format(ano))

elif idade> 18 and genero == 1:
    faltam = idade - 18
    ano = a - faltam
    print('vc esta em debito com o serviço militar\n'
          'seu alistamento foi à {} anos atras'.format(faltam))
    print('seu alitamento foi em {}'.format(ano))
elif genero == 2 :
    print('vc esta dispensada do servico MILITAR OBRIGATORIO!')
