class Pessoa:
    __nome = ""
    __idade = 0
    __peso = 0.0
    __altura = 0.0
    __imc = 0.0
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.calc_imc()
    def calc_imc(self):
        self.__imc = self.__peso/(self.__altura*self.__altura)
        print(self.__imc)
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_peso(self):
        return self.__peso
    def get_altura(self):
        return self.__altura
    def get_imc(self):
        return self.__imc
    def set_nome(self, nome):
        self.__nome = nome
    def set_idade(self, idade):
        self.__idade = idade
    def set_peso(self, peso):
        self.__peso = peso
    def set_altura(self, altura):
        self.__altura = altura
    def set_imc(self, imc):
        self.__imc = imc

class IMC:
    def conf_imc(self, imc):
        if(imc <= 18.5):
            print('Imc abaixo do peso')
        elif(imc <= 25):
            print('Peso normal')
        elif(imc <= 30):
            print('Sobrepeso')
        elif(imc <= 35):
            print('Obesidade')

if __name__ == '__main__':
    imc = IMC()
    pes=Pessoa('Vitor',18,68,1.80)
    