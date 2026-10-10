import customtkinter as ctk
import time

app = ctk.CTk()
#cria um objeto do tipo janela desktop usando a biblioteca customtkinter

app.title("Minha calculadora")
app.geometry("500x600")
#configura o titulo e tamanho da janela do objeto app

visor = ctk.CTkEntry(app,width=500,height=100,placeholder_text="0",font=("Arial",50),justify="right") 
visor.pack(pady=20)
#cria um objeto do tipo entrada de texto (visor) e adiciona ele na janela app

def clicar_botao(valor):
    visor.insert(ctk.END, valor)
#define a função que insere o valor do botão no visor, no final do texto ja existente

frame = ctk.CTkFrame(app)
frame.pack(pady=10)
#cria um objeto frame pois ja existe um pack no visor, portanto o grid tem que ser usado nem um objeto frame, cujo os botões serão filhos e adiciona na janela app

numeros = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
for i, numero in enumerate(numeros):
    botao = ctk.CTkButton(frame, text=numero, width=120, height=100, command=lambda n=numero: clicar_botao(n))
    botao.grid(row=i//3, column=i%3)
#cria os botões de 1 a 9 em uma malha quadriculada pertencente ao frame, usando um loop para evitar repetição de código

primeiro_num=None
op=None

def selecionar_op(operacao):
    global primeiro_num, op

    texto = visor.get()
    if texto == "":
        return
    primeiro_num = float(texto)
    op = operacao
    visor.delete(0, ctk.END)
#função que seleciona a operação, armazena o primeiro número e a operação e depois limpa o visor, caso o visor esteja vazio, a função retorna sem fazer nada

def calcular():
    global primeiro_num, op
    if primeiro_num is None or op is None:
        return
    texto = visor.get()
    if texto == "":
        return
    segundo_num = float(texto)
    resultado = None

    if op == "+":
        resultado = primeiro_num + segundo_num
    elif op == "-":
        resultado = primeiro_num - segundo_num
    elif op == "x":
        resultado = primeiro_num * segundo_num
    elif op == "/":
        if segundo_num != 0:
            resultado = primeiro_num / segundo_num
        else:
            visor.delete(0, ctk.END)
            visor.insert(ctk.END, "Erro")
            app.after(4000, lambda: visor.delete(0, ctk.END))  # Limpa o visor após 4 segundos
            primeiro_num = None
            op = None
            return
    visor.delete(0, ctk.END)
    if resultado.is_integer():
        resultado = int(resultado)
    visor.insert(ctk.END, str(resultado))
    primeiro_num = None
    op = None
#função que realiza o cálculo e exibe o resultado no visor, caso o vizor esteja vazio ou não tenha sido selecionado primeiro número e operação, a função é interrompida, caso tenha uma divião por zero, o visor imprime erro e limpa após 4 segundo, caso o resultado seja inteiro, o .0 é removido do final do número, e o visor é atualizado com o resultado, e as variáveis primeiro_num e op são resetadas para None


botaosum = ctk.CTkButton(frame, text="+",width=120,height=100, command=lambda : selecionar_op("+"))
botaosum.grid(row=0, column=3)



botaox = ctk.CTkButton(frame, text="x",width=120,height=100, command=lambda : selecionar_op("x"))
botaox.grid(row=1, column=3)

botaominus = ctk.CTkButton(frame, text="-",width=120,height=100, command=lambda : selecionar_op("-"))
botaominus.grid(row=2, column=3)

botao0 = ctk.CTkButton(frame, text="0",width=120,height=100,command=lambda : clicar_botao("0"))
botao0.grid(row=3, column=1)

botaopoint = ctk.CTkButton(frame, text=".",width=120,height=100,command=lambda : clicar_botao("."))
botaopoint.grid(row=3, column=0)

botaoresult = ctk.CTkButton(frame, text="=",width=120,height=100, command=calcular)
botaoresult.grid(row=3, column=2)

botaodiv = ctk.CTkButton(frame, text="/",width=120,height=100, command=lambda : selecionar_op("/"))
botaodiv.grid(row=3, column=3)

app.mainloop()
#roda o loop principal da janela app, mantendo a janela aberta e aguardando interações do usuário