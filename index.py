class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f'O aluno {self.nome} está presente.'

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        result = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n'
        for aluno in self.alunos:
            result += aluno.presenca() + '\n'
        return result

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}.'

professor = Professor("Mario")
print(professor.ministrar_aula("Programação Orientada a Objetos"))

aluno1 = Aluno("João")
aluno2 = Aluno("Fábio")
aluno3 = Aluno("Mariana")

aula = Aula(professor, "Programação Orientada a Objetos", [])

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.adicionar_aluno(aluno3)

print(aula.listar_presenca())
