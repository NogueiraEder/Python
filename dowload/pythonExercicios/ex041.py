from datetime import date

d =int(input('informe o ano de nascimento do atleta'))
atual = date.today().year
idade =atual - d
if idade <= 9:
    print('Mirim')
elif idade >9 and idade <=14:
    print('Infantil')
elif idade > 14 and idade <=19:
    print('Junio')
elif idade >19 and idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')
