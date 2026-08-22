from abc import ABC, abstractmethod

class Livro:
    def __init__(self, titulo, autor, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f'{self.titulo} foi emprestado')
        else:
            print(f'{self.titulo} já está emprestado')

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f'{self.titulo} foi devolvido')
        else:
            print(f'{self.titulo} não está emprestado')

class Biblioteca:
    def __init__(self):
        self.lista =[]
    
    def addlivro(self,novolivro):
        self.lista.append(novolivro)
        print(f'{novolivro.titulo} adicionado na biblioteca')

    def listarlivros(self):
        for livros in self.lista:
            print(f'{livros.titulo} : {livros.autor}')

    def listardisponiveis(self):
        print('livros disponíveis na biblioteca:')
        for livros in self.lista:
            if livros.disponivel == True:
                print(livros.titulo)
            else:
                pass

class Usuario(ABC):
    def __init__(self,nome):
        self.nome = nome
        self.listaemprestimos = []

    def pegarlivro(self,alvo):
        if alvo.disponivel == True and len(self.listaemprestimos)<self.limite():
            self.listaemprestimos.append(alvo)
            alvo.disponivel = False
            print(f'{self.nome} pegou {alvo.titulo} emprestado')
        elif len(self.listaemprestimos)==self.limite():
            print('você já pegou o max de livros emprestados')
        else:
            print(f'{alvo.titulo} ja está emprestado')


    def devolverlivro(self,alvo):
        if alvo.disponivel == False:
            self.listaemprestimos.remove(alvo)
            alvo.disponivel = True
            print(f'{self.nome} devolveu {alvo.titulo}')
        else:
            print(f'{alvo.titulo} já está disponível')

    def listar(self):
        print(f'livros emprestados a {self.nome}:')
        for livros in self.listaemprestimos:
            print(f'{livros.titulo}')

    @abstractmethod
    def limite(self):
        pass

class Aluno(Usuario):

    def limite(self):
        return 3
    
class Professor(Usuario):

    def limite(self):
        return 5
    

Diego=Aluno('Diego')
Biblioteca = Biblioteca()
l1 = Livro('Cortiço','Aluísio')
l2=Livro('Donquixote','nsei')
l3=Livro('Escrava','Firmina')
l4=Livro('Biblia','Jesus')


Biblioteca.addlivro(l1)
Biblioteca.addlivro(l2)
Biblioteca.addlivro(l3)
Biblioteca.addlivro(l4)
Biblioteca.listarlivros()


Diego.pegarlivro(l1)
Diego.pegarlivro(l1)
Diego.pegarlivro(l2)
Diego.pegarlivro(l3)
Diego.pegarlivro(l4)

Diego.devolverlivro(l3)
Diego.pegarlivro(l4)

Diego.listar()

Biblioteca.listardisponiveis()