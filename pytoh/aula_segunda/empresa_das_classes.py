
from random import randint

class Funcionario:
    codigo = 0
    horas = 0.0
    valor_hora = 0.0
    valor_salario = 0.0
    quantidade_horas_extra = 0.0
    salario_total = 0.0
    def __init__(self, codigo,hora,valor_hora,quantidade_horas):
        self.codigo= codigo
        self.horas = hora
        self.valor_hora = valor_hora
        self.quantidade_horas_extra = quantidade_horas
    def calcular_hora_extra(self):
        val_extra = (self.valor_hora*1.5)*self.quantidade_horas_extra
        return val_extra
    def calcular_salario_total(self):
        total = (self.horas*self.valor_hora)+self.calcular_hora_extra()
        self.salario_total = total
        return total
    def mostrar_funcionario(self):
        print('Codigo:', self.codigo,'Horas trabalhadas: ', self.horas, 'Salario: ', self.salario_total)
class FolhaPagamento:
    funcionarios = []
    def ordenar_crescente(self):
        self.funcionarios.sort(reverse = True, key=lambda x: x.salario_total)
    def mostrar_funcionarios(self):
        for i in self.funcionarios:
            i.mostrar_funcionario()

if __name__ == '__main__':
    oo = FolhaPagamento()
    for i in range(10):
        new_funcionario = Funcionario(randint(0,77), randint(0,77),randint(100,800),randint(100,800))
        new_funcionario.calcular_salario_total()
        oo.funcionarios.append(new_funcionario)
    oo.mostrar_funcionarios()
    print("-----------------------")
    oo.ordenar_crescente()
    oo.mostrar_funcionarios()