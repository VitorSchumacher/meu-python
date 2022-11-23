def add_rep(rep,num):
    for i in rep:
        if i == 0:
            i = num

            return
    print ("Lista cheia")
    return False


def achar_men(lista,tam,rep):
    men = lista[0]
    pos = 0
    if tam > 11 : 
        return 981
    for i in range(6):
        if lista[i] < men:
            men = lista[i]
            pos = i
    print(tam)
    if lista[tam] < men:
        add_rep(rep,lista[tam])
        lista[tam] = 0
        return False
    else:
        lista[pos],lista[tam] = lista[tam], 0
    
    return men

def valida_mem_sec(lista):
    for i in lista:
        if i == 0:
            return True
    return False

        

if __name__ == '__main__':
    tam = 6
    lista = [29,14,76,75,59,6,7,74,58,46,10,18]
    part1 = [0,0,0,0,0,0]
    part2 = [0,0,0,0,0,0]
    rep = [0,0,0,0,0,0]

    for i in range(0,10): 
        if valida_mem_sec(part1) == True:
            aux = achar_men(lista,tam,rep)
            if aux == False:
                print("colocado na outra lista")
            elif aux == 981:
                tam = -1
                i = 0
            else:
                part1[i] = aux
            tam += 1
        elif valida_mem_sec(part2) == True:
            aux = achar_men(lista,tam,rep)
            if aux == False:
                print("colocado na outra lista")
            else:
                part2[i] = aux
            tam += 1
    print (lista)
    print (part1)
    print (part2)
    print (rep)




