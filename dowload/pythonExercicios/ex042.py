print('-='*20)
print('\033[1;32m ANALIZADOR DE TRIÂNGULOS!! \033[m')
print('-='*20)

a = float(input('Informe o Primeiro lado do Triângulo'))
b = float(input('Informe o Segundo lado do Triângulo'))
c = float(input('Informe o Terceiro lado do Triângulo'))
# | b - c | < a < b + c
result = abs(b-c) < a < (b + c)
if result == True:
    print('\033[1;32mO Triângo Poderá ser Formado\033[m!!')
    if a == b == c:
        print('o triangulo será\033[1;34m <<EQUILÁTERO>>\033[m')
    elif a != b != c:
        print('o triangulo será \033[1;34m<<ESCALENO>>\033[m')
    elif a == b != c or a==c!=b or b == c != a:
        print('o triangulo será \033[1;34m<<ISÓCELES>>\033[m')
else:
    print('\033[1;33mNÃO SERÁ POSSIVEL A FORMAÇÃO DESSE TRIANGULO\033[m!\nTENTE ADEQUAR OS VALORES!!')
