class Motor:
    _tipo_comb = ""
    def consumir_combustivel(self):
        print("Consumindo")
    def em_funcionamento(self):
        print("Funcionamento")
    def __init__(self,tipo):
        self._tipo_comb = tipo
class Triflex: 
    _motor1 = []
    _motor2 = []
    _motor3 = []
    def __init__(self,motor1,motor2,motor3):
        self._motor1 = motor1
        self._motor2 = motor2
        self._motor3 = motor3
    def consumir_combustivel(self):
        print ("Consumindo")

if __name__ == '__main__':
    gasolina = Motor("gasolina")
    alcool = Motor("alcool")
    gas = Motor("gas")
    carro = Triflex(gasolina, alcool, gas)

        