lista=[]
dados=[]
ordem=[]
while True:
    dados.append(str(input('nome do aluno: ')))
    ordem.append(float(input('nota 1: ')))
    ordem.append(float(input('nota 2: ')))
    dados.append(ordem[:])
    lista.append(dados[:])
    ordem.clear()
    dados.clear()
    x=input('quer continuar? [S/N]: ').upper()
    while x != 'S' and x !='N':
        x = input('digite novamente [S/N]: ').upper()
    if x == 'S':
        pass
    elif x == 'N':
        break
print('-=-'*12)
print('No. NOME             MÉDIA')
print('-'*36)
for x in range(0,len(lista)):
    média=(lista[x][1][0]+lista[x][1][1])/2
    print(f'{x:<2} {lista[x][0]:<10} {média:>12}')
while True:
    print('-'*36)
    y=int(input('diga o número do aluno para saber as notas (999 encerra o programa): '))
    while y != 999 and y>len(lista)-1:
        y = int(input('número inválido, digite novamente: '))
    if y == 999:
        print('programa encerrado')
        break
    elif y<len(lista) and y != 999:
        print(f'as notas de {lista[y][0]} são {lista[y][1][0]} e {lista[y][1][1]}')
