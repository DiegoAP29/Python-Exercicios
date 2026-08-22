x = ('hambúrguer sorvete salada milkshake').split()
a=b=c=d=s=0
import time
e = 14.50
f = 4.50
g = 17.80
h = 12.00
print('==='*10)
print('Cardápio')
while True:
    print('Aperte [0] para acrescentar um hámburguer(R$14.50) na compra: ')
    print('Aperte [1] para acrescentar um sorvete(R$4.50) na compra: ')
    print('Aperte [2] para acrescentar uma salada(R$17.80) na compra: ')
    print('Aperte [3] para acrescentar milkshake(R$12.00) na compra: ')
    print('Aperte [4] para encerrar seu pedido: ')
    print('==='*10)
    y = int(input('Escolha uma opção: '))
    if y == 4:
        break
    elif -1<y<4:
            if y == 0:
                 a +=1
                 print(f'você adicionou um {x[0]} no seu pedido')
                 s = s + e
            elif y ==1:
                 b +=1
                 print(f'você adicionou um {x[1]} no seu pedido')
                 s = s+ f
            elif y ==2:
                 c+=1
                 print(f'você adicionou um {x[2]} no seu pedido')
                 s = s+g
            else:
                 print(f'você adicionou um {x[3]} no seu pedido')
                 d+=1
                 s = s+h
    else:
        print('inválido, escolha novamente: ')
    print('')
    time.sleep(1)
if a == 1:
     print(f'você pediu {a} hambúrguer')
elif a > 1:
     print(f'você pediu {a} hambúrgueres')
else:
     pass
if b == 1:
     print(f'você pediu {b} sorvete')
elif b>1:
     print(f'você pediu {b} sorvetes')
else:
     pass
if c == 1:
     print(f' você pediu {c} salada')
elif c> 1:
     print(f' você pediu {c} saladas')
else:
     pass
if d == 1:
     print(f'você pediu {d} milkshake')
elif d>1:
     print(f'você pediu {d} milkshakes')
print(f'O total deu R${s:.2f}')
time.sleep(10)