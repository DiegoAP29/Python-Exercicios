x = 0
a = int(input('número 1: '))
b = int(input('número 2: '))
import time
while x != 5:
    print('aperte [1] pra somar os números')
    print('aperte [2] para mutiplicar os números')
    print('aperte [3] para saber qual o maior número')
    print('aperte [4] para escolher novos números')
    print('aperte [5] para encerrar o programa')
    x = int(input('escolha uma opção: '))
    if x == 1:
        print(f'a soma de {a} com {b} é {a+b}')
    elif x == 2:
        print(f' a mutiplicação de {a} com {b} é {a*b}')
    elif x == 3 and a>b:
        print(f' o maior número entre {a} e {b} é {a}')
    elif x == 3 and b>a:
        print(f' o maior número entre {a} e {b} é {b}')
    elif x == 4:
        a = int(input('digite um novo valor de número 1: '))
        b = int(input('digite um novo valor de número 2: '))
        pass
    elif x == 5:
        print('programa encerrado')
    else:
        print('inválido')
    if x != 5:
        print('')
        print('aguarde o menu reaparecer')
        time.sleep(3)
        print('')
    else:
        pass