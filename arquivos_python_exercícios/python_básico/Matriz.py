lista=[[0,0,0],[0,0,0],[0,0,0]]
tot=tot2=maior= 0
for c in range(0,3):
    for d in range(0,3):
        lista[c][d]=int(input(f'núm na posição ({c},{d}): '))
for e in range(0,3):
    for f in range(0,3):
        print(f'[{lista[e][f]:^5}]',end='')
    print()
for g in range(0,3):
    for h in range(0,3):
        if lista[g][h]%2 == 0:
            tot += lista[g][h]
        else:
            pass
print(f'{tot} é a soma dos pares')
for j in range(0,3):
    tot2 +=lista[j][2]
print(f'{tot2} é a soma da coluna 2')
for z in range(0,3):
    if lista[1][z]>maior:
        maior=lista[1][z]
print(f'o maior valor da linha 1 é {maior}')