class Aluno:
    nota_um = 0
    nota_dois = 0
    media = 0

    def calcular_media(self):
        self.media = (self.nota_um + self.nota_dois) / 2
    def inserir_nota(self):
        self.nota_um = float(input("Nota um"))
        self.nota_dois = float(input("Nota dois"))
    
class Turma:
    alunos = []
    def inserir_alunos(self):
        aluno = Aluno()
        aluno.inserir_nota()
        aluno.calcular_media()
        self.alunos.append(aluno)
    def calcular_media_turma(self):
        media = 0.0
        cont = 0
        for i in self.alunos:
            media += i.media
            cont+=1
        media = media/cont
        return media

if __name__ == '__main__':
    turma_hoje = Turma()
    for x in range(2):
        turma_hoje.inserir_alunos()
    print('media = ', turma_hoje.calcular_media_turma)
