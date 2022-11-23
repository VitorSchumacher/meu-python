class Date:
    dia = 0
    mes = 0
    ano = 0

    def __init__(self, dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def comp_ano(self,data2):
        if self.ano > data2.ano:
            print("Data 1 é mais recente")
            return True
        elif self.ano < data2.ano:
            print("Data 2 é mais recente")
            return False
        elif self.ano == data2.ano and self.mes > data2.mes:
            print("Data 1 é mais recente")
            return True
        elif self.ano == data2.ano and self.mes < data2.mes:
            print("Data 2 é mais recente")
            return False
        elif self.ano == data2.ano and self.mes == data2.mes and self.dia > data2.dia :
            print("Data 1 é mais recente")
            return True
        elif self.ano == data2.ano and self.mes == data2.mes and self.dia < data2.dia :
            print("Data 2 é mais recente")
            return False
        else :
            print("As datas são iguais")
            return True
            

if __name__ == "__main__":
    data1 = Date(20,3,2003)
    data2 = Date(20,3,2003)
    data1.comp_ano(data2)
