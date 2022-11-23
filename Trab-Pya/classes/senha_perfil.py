class Senha_perfil():
    __nome = ""
    __senha = ""

    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome
    @property
    def senha(self):
        return self.__senha