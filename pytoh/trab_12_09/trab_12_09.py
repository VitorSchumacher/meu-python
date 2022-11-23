import abc

class Veiculo(abc.ABC):
    @abc.abstractmethod
    def listarVerificacion(self):
        pass
    @abc.abstractmethod
    def ajustar(self):
        pass
    @abc.abstractmethod
    def limpar(self):
        pass

class Bicicleta(Veiculo):
    def listarVerificacion(self):
        print("Verificada")
    def ajustar(self):
        print("Ajustada")
    def limpar(self):
        print("Limpa")

class Automovel(Veiculo):
    def listarVerificacion(self):
        print("Verificada")
    def ajustar(self):
        print("Ajustada")
    def limpar(self):
        print("Limpa")
    def mudarOleo(self):
        print("Mudado")

bmw = Automovel()
bmw.limpar()
