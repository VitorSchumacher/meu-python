class Aluno:
    g1 = 0.0
    g2 = 0.0
    media = 0.0
    def calcular_media(self):
        self.media = (self.g1 + self.g2) / 2.0
    def inserir_notas(self):
        self.g1 = float(input('informe a nota 1: '))
        self.g2 = float(input('informe a nota 2: '))
class Turmas:
    alunos = []
    def inserirAlunas(self):
        aluno = Aluno()
        aluno.inserir_notas()
        aluno.calcular_media()
        self.alunos.append(aluno)
    def calcular_media_turma(self):
        media = 0.0
        cont = 0
        for cada in self.alunos:
            media += cada.media
            cont += 1
        media = media/cont
        return media

if __name__ == '__main__':
    oo = Turmas()
    for x in range(4):
        