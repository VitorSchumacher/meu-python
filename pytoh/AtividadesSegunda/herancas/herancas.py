class Veiculo:
    def andar(self):
        print("andei")
class Carro(Veiculo):
    _nrodas = 4

gol = Carro()
gol.andar()