ord = list()
menor=maior =cont=0
for i in range(0,5):
    n = int(input('Digite um valor'))
    if i == 0:
        ord.append(n)
        print('aad ao final da lista')
    elif n > ord[-1]:
        ord.append(n)
    else:
        # aqui ele ira cair nesse laço para verificar em cada posicao o menor
        # e imserir nessa posicao.
        # enquanto a contagem for menor que o tamanho da lista repita
        # (while cont <len(ord):)
        # se numero add(n)  for menor igual ao numero na posicao da contagem
        # entao:(if n <= ord[cont]:)
        # insira o n nessa possicao:(ord.insert(cont,n))
        # manda finalizar p loop e voltar a pergunta com outro varlor ça no for
        # e soma 1 a contagem - se nao ele vai ficar nao contagem ate ela acaar
        # e nao fara isso com os proximos valores


        while cont <len(ord):
            if n <= ord[cont]:
                ord.insert(cont,n)
                break
            print(ord)
            cont+=1


print(ord)