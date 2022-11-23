print("teste")

class Aluno:
    nome = ''
    sobrenome = ''
    CPF = ''
    def __init__(self, nome, sobrenome):
        
    def responder(self,text):
        print(text)
    def alterar_nome(self):
        self.nome = input('Digite seu nome')
        print("Nome alterado para:",self.nome)

class Diciplina:
    professor = ''
    nome = ''
    monitor = ''

class Curso:
    nome = ''
    carga_horaria = 0 
    dif_foi = ''

class Professor:
    nome = ''
    formação = ''
    salario = ''


alunoUm = Aluno()
alunoUm.nome = 'Toni PikaChu'
alunoUm.sobrenome = 'Da Quebra'
alunoUm.CPF = '111111111'

alunoUm.responder(text='Estou Presente aqui na aula')
alunoUm.alterar_nome()
print(alunoUm.nome)
