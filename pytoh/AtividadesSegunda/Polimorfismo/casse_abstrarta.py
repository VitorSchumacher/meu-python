import abc
from ast import Pass
class Funcionario(abc.ABC):
    _name = ''
    _cpf = ''
    _salary = 0
    _bonific = 0
    def __init__(self, name, cpf, salary):
        self._name = name
        self._cpf = cpf
        self._salary = salary
    @abc.abstractmethod
    def get_bonificacao(self):
        Pass
class Generete(Funcionario):
    # outros metodos e props
    def get_bonificacao(self):
        return self._salario*0.15
class Diretor(Funcionario):
    def __init__(self, nome, cpf,salario):
        super().__init__(self,nome,cpf,salario)
    def get_bonificacao(self):
        self._bonific = self._salary *1.25

if __name__ == '__main__':
    diretor = Diretor('joão', '11111-1111', 4000)