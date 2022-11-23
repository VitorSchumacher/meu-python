class Aux:
    value = 0
    fdir = {}
    fesq = {}
class Filho:
    value = 0
    fdir = Aux
    fesq = Aux
    def __init__(self,value):
        self.value = value
        self.fdir = None
        self.fesq = None

class Arvore:
    raiz = Filho

    def __init__(self,folha):
        self.raiz = folha


def addNewFolha(raiz,folha):
    if raiz == None:
        raiz.raiz = folha
    elif raiz.raiz.value > folha.value:
        if raiz.raiz.fdir == None:
            raiz.raiz.fdir = folha.value
        else:
            addNewFolha(raiz.raiz.fdir,folha)
    elif raiz.raiz.value < folha.value:
        if raiz.raiz.fesq == None:
            raiz.raiz.fesq = folha
        else:
            addNewFolha(raiz.raiz.fesq,folha)



def mostrarArvore(raiz):
    if raiz == None :
        return
    mostrarArvore(raiz.fesq)
    print(raiz.value)
    mostrarArvore(raiz.fdir)



if __name__ == '__main__':
    x = int(input("digite seu numero:"))
    newFolha = Filho(x)
    arvore = Arvore(newFolha)
    while True:
        x = int(input("digite seu numero:"))
        newFolha = Filho(x)
        addNewFolha(arvore, newFolha)
        # mostrarArvore(arvore)
