class Student:
    __name = ''
    __answers = []
    __note = 0.0
    __correct = 0
    def __init__(self, name) :
        self.__name = name
        for i in range(20):
            self.__answers.append(int(input('Resposta %d: ' % (i+1))))
    def calc_correct(self, feedback):
        for i in range(0,len(feedback)):
            if feedback[i] == self.__answers[i]:
                self.__correct += 1
        self.calc_note()
    def calc_note(self):
        self.__note = (self.__correct - (20-self.__correct)/2)/2
        print(self.__note)
        if self.__note >= 5:
            print("APROVADO")
        else: 
            print("REPROVADO")

class Class :
    __feedback = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    __student = []
    @property
    def feedback(self):
        return self.__feedback
    @property
    def student(self):
        return self.__student

if __name__ == '__main__':
    class1 = Class()
    studant1 = Student('Pedro')
    studant1.calc_correct(class1.feedback)
    class1.student.append(studant1)