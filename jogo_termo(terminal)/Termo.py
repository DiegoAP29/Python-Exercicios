from lista import PALAVRAS
import random
import unicodedata

def remover_acentos(palavra):
    palavra = unicodedata.normalize("NFD", palavra)
    return "".join(
        letra for letra in palavra
        if unicodedata.category(letra) != "Mn"
    )

palavra_secreta = random.choice(PALAVRAS)
palavra_secretamodificada = remover_acentos(palavra_secreta)
print(13*" ","TERMO")
print("-"*31)
print("Digite uma palavra de 5 letras, você tem 6 tentativas: ")
tentativas = 0

while tentativas != 6:
    chutecru = str(input("")).lower().strip()
    chute = remover_acentos(chutecru)

    while len(chute) != 5 or not all(letra.isalpha() for letra in chute):
        print("Digite uma palavra somente de 5 letras")
        chute = str(input("")).lower().strip()

    for i, letra in enumerate(chute):
        if letra == palavra_secretamodificada[i]:
            print("🟩",end="")
        elif letra in palavra_secretamodificada:
            print("🟨",end="")
        else:
            print("⬛",end="")

    print("")
    if chute == palavra_secretamodificada:
        print(f"Acertou!! Plavra era: {palavra_secreta}, Jogo encerrado!")
        break
    tentativas +=1
if tentativas == 6:
    print(f"Fim das tentativas, a palavra era {palavra_secreta}! tente novamente")