global loop 
loop = 0

def divide(lista, start, end):
    global loop
    pivo=lista[start]
    next = start + 1
    last = end
    while True:
        while next <= last and lista[last] >= pivo:
            last -= 1
            loop +=1
        while next <= last and lista[next] <= pivo:
            loop +=1
            next += 1
        if next <= last:
            lista[next], lista[last] = lista[last], lista[next]
        else:
            break
    lista[start],lista[last] = lista[last], lista[start]
    return last
def quicksort(lista,start,end):
    global loop
    loop +=1
    if start >= end:
        return
    p=divide(lista,start,end)
    quicksort(lista,start,p-1)
    quicksort(lista,p+1,end)

def busca_binaria(lista,busca,ini,fim):
    mid = (ini+fim) // 2
    if ini>fim:
        return -1
    if lista[mid] == busca:
        print(lista[mid])
        return lista[mid]
    elif lista[mid] < busca:
        return busca_binaria(lista,busca,mid+1,fim)
    elif lista[mid] > busca:
        return busca_binaria(lista,busca,ini,mid-1)


if __name__ == '__main__':
    lista = [8,6,2,9,1,4,5]
    print(lista)
    quicksort(lista,0,len(lista)-1)
    print(lista)
    busca_binaria(lista,100,0,len(lista)-1)

