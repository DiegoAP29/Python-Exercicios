class Carro:
    def __init__(self,velocidade = 0,estado=False):
        self.velocidade = velocidade
        self.estado = estado

    def ligar(self):
        if self.estado == False:
            print('O carro está desligado, ligando o carro...')
            self.estado = True
        else:
            print('O carro já está ligado!')

    def desligar(self):
        if self.estado == True:
            print('O carro está ligado, desligando o carro...')
            self.estado = False

            self.velocidade = 0
        else:
            print('O carro já está desligado!')

    def acelerar(self):
        if self.estado == False:
            self.ligar()

        while True:
            x=int(input('Digite a velocidade que deseja acelerar: '))
            if x <0:
                print('A velocidade que você deseja acelerar é menor do que 0!')
            else:
                self.velocidade += x
                break

    def frear(self):
        if self.estado == False:
            self.ligar()   

        while True:
            x=int(input('Digite a velocidade que deseja frear: '))
            if x <0 or x > self.velocidade:
                print('A velocidade que você deseja frear é menor do que 0 ou maior do que a velocidade atual do carro!')
            else:
                break


        self.velocidade -= x

    def mostrar_velocidade(self):
        print(f'A velocidade atual do carro é: {self.velocidade} km/h')

sandero = Carro()

sandero.acelerar()

sandero.frear()

sandero.mostrar_velocidade()

sandero.desligar()

sandero.mostrar_velocidade()