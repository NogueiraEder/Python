nome = str(input('escreva seu nome completo'.strip()))
print(nome.upper())
print(nome.lower())
print('seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro  nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa[0].capitalize(),# len(separa[0]),('letras'))