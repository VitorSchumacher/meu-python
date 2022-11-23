
def ler_numeros(vet):
    tam = int(input("numero de elementos: "))
    for x in range(tam):
        #inset é para inserir em um vetor, esta na casa 0 para add no inicio
        #para add no final colocar len(nome_vetor)
        vet.insert(0, int(input("numeros: ")))


if __name__ == '__main__':
    vet = []
    ler_numeros(vet)
    print(vet)

