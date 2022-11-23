# errado
def shakershort(lista):
    tam = len(lista)-1
    maior = lista[0]
    menor = lista[0]
    for x in range(0,int(tam/2)):
        troca=0
        maior = lista[x]
        menor = lista[tam-x]
        for i in range(x,tam-x):
            print(i)
            if maior<lista[i]:
                maior = lista[i]
                posMai = i
                troca=1
            if menor>lista[i]:
                menor = lista[i]
                troca=1
                posMen = i
        if(troca==1):
            lista[x],lista[tam-x],lista[posMen],lista[posMai]=lista[posMen],lista[posMai],lista[x],lista[tam-x]
        print(lista)
    
    





if __name__ == '__main__':
    lista = [8,6,2,9,1,4,5,3]
    print(lista)
    shakershort(lista)
    print(lista)