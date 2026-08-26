x = int(input('\033[32mQuantas frases você quer digitar? \033[m'))
print('-'*40)
for i in range(x):
    frase = input('Digite a frase: ')
    print('-'*40)
    with open('arquivos_python_exercícios/python_básico/arquivo_texto', 'a', encoding='utf-8') as file:
        file.write(f'{frase}\n')

print('\033[34mAs frases digitadas nesse programa foram:\033[m')
with open('arquivos_python_exercícios/python_básico/arquivo_texto', 'r', encoding='utf-8') as file:
    conteudo = file.read()
    print(conteudo)