r1=0
r2=1
x=int(input('quantos termos da sequência de fibonacci: '))
if x==1:
    print(r1)
if x==2:
    print(r1)
    print(r2)
else:
    print(r1)
    print(r2)
    for c in range(0,x-2):
        r3= r1+r2
        r1=r2
        r2=r3
        print(r3)
