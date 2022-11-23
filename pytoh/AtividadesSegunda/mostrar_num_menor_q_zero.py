def ler_numeros(vet):
    tam = int(input("numero de elementos: "))
    for x in range(tam):
        vet.insert(len(vet), int(input("numeros: ")))

def mostrar_num_menor_q_zero(vet):
    for x in range(len(vet)):
        if vet[x] < 0:
            print("posicão vet[%d]" % x)

if __name__ == '__main__':
    vet = []
    ler_numeros(vet)
    print(vet)
    mostrar_num_menor_q_zero(vet)
