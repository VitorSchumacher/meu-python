class Conteudo():
    __nome=''
    props = []

    def __init__(self, nome,props):
        self.__nome=nome
        self.props=props

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome=value
