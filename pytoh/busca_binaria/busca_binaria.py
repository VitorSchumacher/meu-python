

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
    list = [2,5,8,10,14,18,22,24,28,30]
    tam = len(list)-1
    busca_binaria(list,2,0,tam)

