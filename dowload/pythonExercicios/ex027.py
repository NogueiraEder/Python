nome = str(input('Digite seu nome!')).strip().lower()
n = nome.split()
print('seu primeiro nome é :{}'.format(n[0]).title())
print('seu ultimo nome é :{}'.format(n[len(n)-1]).title())