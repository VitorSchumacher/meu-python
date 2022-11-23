

from xml.etree.ElementTree import tostring


class Ponto:
    def desenhar(self): return "*"

class Reta(Ponto):
    def desenhar(self): 
        print(''+super().desenhar()+''+super().desenhar())
    
class Triangulo(Ponto):
    def desenhar(self):
        for i in range(0,2):
            if i == 0:
                print(''+super().desenhar())
            else:
                print(''+super().desenhar()+''+super().desenhar())

class Quadrado(Ponto):
    def desenhar(self): 
        for i in range(2):
            print(''+super().desenhar()+''+super().desenhar())
    

def fazerArte(func):
    func.desenhar()

um = Quadrado()
dois = Reta()
tres = Triangulo()

fazerArte(um)
fazerArte(tres) 
fazerArte(dois) 