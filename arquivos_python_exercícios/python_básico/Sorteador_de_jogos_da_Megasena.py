print('='*30)
print('JOGO DA MEGA SENA')
print('='*30)
lista=[]
dados=[]
x = int(input('Quantos jogos você quer sortear? '))
import random
import time
print(f'Sorteio dos {x} jogos')
for c in range(0,x):
    dados = random.sample(range(1,61), 6)
    if dados in lista:
        pass
    else:
        lista.append(dados[:])
    dados.clear()
    lista[c].sort()
    print(f'Jogo {c+1}: {lista[c]}')
    time.sleep(2)