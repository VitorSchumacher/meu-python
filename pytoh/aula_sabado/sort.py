def ordenar_sort(vet,vet_ord):
    repite =1
    repites = 1
    for x in range(0,len(vet)):
        repites = 1
        if repite ==1:
            vet_ord.insert(x-1,vet[x-1])
        while repites ==1:
            print("oiç")
            if vet_ord[x] > vet_ord[x-1]:
                print("oi")
                aux = vet_ord[x-1]
                vet_ord[x-1]=vet_ord[x]
                vet_ord[x] =aux
                x-=1
                repite=0
                repites = 1
            else:
                repite=1
                repites = 0

if __name__ == '__main__':
    vet = []
    vet_ord = []
    for x in range(6):
        vet.insert(len(vet), int(input("Seu valor: ")))
    print(vet)
    ordenar_sort(vet,vet_ord)
    print(vet_ord)
    

