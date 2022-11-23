class EntradaDeCinema:
    _nomeDoFilme = ''
    _horário = 0.0
    _sala = 0
    _valor = 0.0
    def __init__(self):
        self._nomeDoFilme = input("Nome do filme: ")
        self._horário = float(input("Horário: "))
        self._sala = int(input("Sala: "))
        self._valor = float(input("Valor: "))
    def calculaDesconto(self,pessoa):
        print(pessoa._idade)
        if(isinstance(pessoa, Estudadente)): 
            if (pessoa._idade<12):
                return 0
            elif (pessoa._idade >= 12 and pessoa._idade <= 15):
                preco = self._valor*0.6
                preco = self.CalculaDescontoHorário(preco)
                return preco
            elif (pessoa._idade >= 16 and pessoa._idade <= 20):
                preco = self._valor*0.7
                preco = self.CalculaDescontoHorário(preco)
                return preco
            elif (pessoa._idade >= 21 ):
                preco = self._valor*0.8
                preco = self.CalculaDescontoHorário(preco)
                return preco
        else:
            precos = self.CalculaDescontoHorário(self._valor)
            return precos
    def exibirIngresso(self):
        print("Nome do filme: ", self._nomeDoFilme)
        print("Horario do filme: ", self._horário)
        print("Sala do filme:", self._sala)
        print("Valr do ingresso: ", self._valor)
    def CalculaDescontoHorário(self,valor):
        if (self._horário <= 16):
            preco = valor*0.9
            return preco
        return valor
class Cliente:
    _nome = ''
    _idade = 0
    def __init__(self):
        self._nome = input("Nome: ")
        self._idade = int(input("Idade: "))

class Estudadente(Cliente):
    _matricula = 0
    def __init__(self):
        super().__init__()
        self._matricula = int(input("Matricula: "))

if __name__ == "__main__":
    filme = EntradaDeCinema()
    pessoa = Estudadente()
    print(filme.calculaDesconto(pessoa))
    pessoa = Cliente()
    print(filme.calculaDesconto(pessoa))
   


