lista=list()
resut= list()
cont=0
ind=0
print('##'*20)
print('         Media alunos 1º Ano')
print('##'*20)

while True:
    h=str(input('Nome: ')).strip().title()
    n1=float(input('1ª Nota: '))
    n2 = float(input('2ª Nota : '))
    lista.append(h)
    lista.append(n1)
    lista.append(n2)
    resut.append(lista[:])
    lista.clear()

    v=str(input('deseja continuar[S/N]')).lower().strip()[0]
    if v in'n':
        break

print('=-='*15)
print(' nº   Nome          Media')
print('--'*20)

for l in resut:
    cont+=1
    media = (l[1] + l[2])/2
    print(f'[0{cont:<}]--{l[0]:<7}      >>{media:>3.1f}')
    print('--'*20)
while not ind == 999:
    print('=-=' * 15)
    ind=int(input('N do aluno para  notas ou(999para sair)\n>>'))
    print(f'As notas '
          f'de {resut[ind-1][0]} sao:'
          f' [ {resut[ind-1][1]} e {resut[ind-1][2]} ]')
