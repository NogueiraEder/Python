# analise de dados maior e menor idade

from datetime import date
hoje= date.today().year
contmaior = 0
contmenor = 0
for c in range(1,8):
    ano =  int(input(f'''informe o ano de nascimento da {c}ª pessoa :'''))
    idade = hoje - ano
    if idade >=21:
        contmaior +=1
    else:
        contmenor +=1
print(f'''{contmaior} pessoas sao maiores de idade''')
print(f'''{contmenor} pessoas sao menor de idade''')