
def ler_numeros(vet):
    for x in range(10):
        vet.insert(len(vet), int(input("numeros: ")))

def troca_lugar_vet(vet):
    for x in range(5):
        aux = vet[x]
        vet[x] = vet[x+5]
        vet[x+5] = aux
if __name__ == '__main__':
    vet = []
    ler_numeros(vet)
    print(vet)
    troca_lugar_vet(vet)
    print(vet)

