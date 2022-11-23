class Classe1:
    def saudacao(self): print("sadação")
class Classe2:
    def saudacao(self): print("crias")

def funcao(obj):
    obj.saudacao()

c1 = Classe1()
c2 = Classe2()

funcao(c1)
funcao(c2)
