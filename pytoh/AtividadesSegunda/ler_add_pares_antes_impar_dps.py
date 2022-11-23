
def ler_numeros(vet):
    cont_par = 0
    for x in range(10):
        num = int(input('Numero: '))
        if num % 2 == 0:
            vet.insert(cont_par, num)
            cont_par += 1
        else:
            vet.insert(len(vet), num)


if __name__ == '__main__':
    vet = []
    ler_numeros(vet)
    print(vet)
