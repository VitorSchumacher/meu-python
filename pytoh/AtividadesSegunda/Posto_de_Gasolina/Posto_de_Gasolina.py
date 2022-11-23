class Bomba:
    __tipo_combustivel = ''
    __valor_litro = 0.0
    __quatidade_litro = 0.0
    def __init__(self):
        self.__tipo_combustivel = input('Tipo do combustivel: ')
        self.__valor_litro = float(input('Valor litro: '))
        self.__quatidade_litro = float(input('Quatidade de litros: '))
    def abastecer_por_valor(self):
        x = float(input('Valor a ser abastecido: '))
        valor = x/self.valor_litro
        if(valor>self.quantidade_litro):
            print("Não a gasolina para realizar este abastecimento na bomba!!!")
            print(self.quantidade_litro)
            return
        else:
            print("Litros abastecido %.2f" % valor)
            self.__quatidade_litro -= valor
            return valor
    def abastecer_por_litro(self):
        x = float(input('Litros a ser abastecido: '))
        if(x>self.quantidade_litro):
            print("Não a gasolina para realizar este abastecimento na bomba!!!")
            print(self.quantidade_litro)
            return
        else:
            self.__quatidade_litro -= x
            valor = x*self.valor_litro
            print("Total a ser pago: %.2f" % valor)
            return valor
    @property
    def valor_litro(self):
        return self.__valor_litro
    @valor_litro.setter
    def valor_litro(self, value):
        self.__valor_litro = value
    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    @tipo_combustivel.setter
    def tipo_combustivel(self, value):
        self.__tipo_combustivel = value
    @property
    def quantidade_litro(self):
        return self.__quatidade_litro
    @quantidade_litro.setter
    def quantidade_litro(self, value):
        self.__quatidade_litro += value
    
    def inform(self):
        print("Tipo de combustivel: %s" % self.tipo_combustivel)
        print("Preço do litro: R$%.3f" % self.valor_litro)
        print("Quantidade de litros: %.2f" % self.quantidade_litro)

if __name__ == '__main__':
    combustivel = Bomba()
    while True:
        print("1-Abastecer dinheiro\n2-Abastecer litros\n3-Total de combustivel disponivel\n4-Adicionar litros de gasolina\n5-Alterar tipo combustivel\n6-Alterar valor combustivel")
        x = int(input("Opção: "))
        if(x == 1):
            combustivel.abastecer_por_valor()
        elif(x == 2):
            combustivel.abastecer_por_litro()
        elif(x == 3):
            combustivel.inform()
            # print(combustivel.quantidade_litro)
        elif(x == 4):
            combustivel.quantidade_litro = float(input("Litros adicionados: "))
            print(combustivel.quantidade_litro)
        elif(x == 5):
            combustivel.tipo_combustivel = input("Novo combustivel: ")
        elif(x==6):
            combustivel.valor_litro = float(input("Novo valor: "))
        else:
            False

