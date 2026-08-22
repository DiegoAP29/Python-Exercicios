nota=[]
x = int(input("Quantas notas você quer inserir? "))
for c in range (1,x+1):
    nota.append(int(input(f"nota({c}): ")))

soma = 0
for d in nota:
    soma += d
    media = soma / len(nota)
print(f"A média das notas é: {media:.2f}")