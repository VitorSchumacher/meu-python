
class No:
    letra = ''
    filhos = []

    def __init__(self, palavra=""):
        self.letra = palavra

    def add_filho(self,no,conteudo):
        print(no)
        print(conteudo)
        no.filhos.append(conteudo)
        return no

    


class Arvore:

    def __init__(self, palavra):
        print(palavra)
        self.add_palavra(palavra)
        
    
    def add_palavra(self,palavra):
        no = No()
        for i in palavra:
            no = no.add_filho(no,i)
        


    def add_filho(self, letra,raiz):
        raiz = [No(letra)]
        print(raiz.filho.letra)
        return raiz

if __name__ == '__main__':
    arvore = Arvore("Carro")
    arvore.add_palavra("Barco")

