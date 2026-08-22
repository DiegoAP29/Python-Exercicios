from abc import ABC, abstractmethod

class Exercicio:
    def __init__(self,nome,series,repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes = repeticoes

    def mostrar(self):
        print(f'Nome do exercício: {self.nome}')
        print(f'Séries: {self.series}')
        print(f'Repetições: {self.repeticoes}')


class Treino:
    def __init__(self,nome,instrutor):
        self.nome = nome
        self.instrutor = instrutor
        self.lista_exercicios = []


    def mostrar_instrutor(self):
        print(f'Instrutor: {self.instrutor.nome}, Especialidade: {self.instrutor.especialidade}')
        
    def adicionar_exercicio(self,exercicio):
        if exercicio not in self.lista_exercicios:
            self.lista_exercicios.append(exercicio)
        else:
            print(f'O exercício {exercicio.nome} já está no treino.')

    def remover_exercicio(self,exercicio):
        if exercicio in self.lista_exercicios:
            self.lista_exercicios.remove(exercicio)
        else:
            print(f'O exercício {exercicio.nome} não está no treino.')

    def mostrar_treino(self):
        print(f'Treino: {self.nome}')
        for exercicio in self.lista_exercicios:
            exercicio.mostrar()
            print('----')

class Plano:
    def __init__(self,tipo,preco):
        self.tipo = tipo
        self.preco = preco
        self.lista_treinos = []

    def adicionar_treino(self,treino):
        if treino not in self.lista_treinos:
            self.lista_treinos.append(treino)
        else:
            print(f'O treino {treino.nome} já está presente no plano.')

    def remover_treino(self,treino):
        if treino in self.lista_treinos:
            self.lista_treinos.remove(treino)
        else:
            print(f'O treino {treino.nome} não está presente no plano.')

    def mostrar_plano(self):
        print(f'Plano: {self.tipo}')
        print(f'Preço: {self.preco}')
        for treino in self.lista_treinos:
            treino.mostrar_treino()
            print('====')

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,plano):
        super().__init__(nome,idade)
        self.plano = plano
    
    def mostrar_plano(self):
        self.plano.mostrar_plano()

    def mostrar_treinos(self):
        for treino in self.plano.lista_treinos:
            treino.mostrar_treino()

class Instrutor(Pessoa):
    def __init__(self,nome,idade,especialidade):
        super().__init__(nome,idade)
        self.especialidade = especialidade

class Academia:
    def __init__(self,nome):
        self.nome = nome
        self.lista_alunos = []

    def matricular_aluno(self,aluno):
        if aluno not in self.lista_alunos:
            self.lista_alunos.append(aluno)
        else:
            print(f'O aluno {aluno.nome} já está matriculado na academia.')

    def remover_aluno(self,aluno):
        if aluno in self.lista_alunos:
            self.lista_alunos.remove(aluno)
        else:
            print(f'O aluno {aluno.nome} não está matriculado na academia.')

    def mostrar_alunos(self):
        print(f'Academia: {self.nome}')
        for aluno in self.lista_alunos:
            print(f'Aluno: {aluno.nome}, Idade: {aluno.idade}')
            print('====')

supino = Exercicio('Supino',5,10)

crucifixo = Exercicio('Crucifixo',5,10)

treinoA = Treino('Treino A',Instrutor('Carlos',30,'Musculação'))

treinoA.adicionar_exercicio(supino)

treinoA.adicionar_exercicio(crucifixo)

premium = Plano('Premium',120)

premium.adicionar_treino(treinoA)

diego = Aluno('Diego',18,premium)

smart = Academia('Smart Fit')

smart.matricular_aluno(diego)

diego.mostrar_treinos()