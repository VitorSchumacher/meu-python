def comb(lista):
    jump = 1.3
    gap = len(lista)
    change = False
    loop = 0
    while gap>1 or change == False:
        gap=int(float(gap)/jump)
        i = 0
        change = False
        while gap+i<len(lista):
            if lista[i]>lista[i+gap]:
                lista[i+gap],lista[i] = lista[i],lista[i+gap]
                change = True
            loop+=1
            i+=1
    print(loop)

if __name__ == '__main__':
    lista = [8,6,2,9,1,4,5]
    print(lista)
    comb(lista)
    print(lista)