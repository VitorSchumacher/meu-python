

def bubble(lista):
    troca = 0
    loop = 0
    while troca == 0:
        troca = 1
        for i in range(0,len(lista)-1):
            if(lista[i]>lista[i+1]):
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
                troca = 0
                loop+=1
            print(lista)
    print(loop)

if __name__ == '__main__':
    lista = [8, 16, 11, 4, 9, 5, 6]
    print(lista)
    bubble(lista)
    print(lista)