import time
dict={}
while True:
    print('-'*40)    
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1- ''\033[34mVer pessoas cadastradas\033[m')
    print('2- ''\033[34mCadastrar nova pessoa\033[m')
    print('3- ''\033[34mSair do sistema\033[m')
    print('-'*40)
    while True:
        opcao=input('\033[32mescolha uma opção: \033[m')
        try: 
            opcao=int(opcao)
        except ValueError:
            print('\033[31mERRO! digite uma opção válida\033[m')
        else:
            if opcao!=1 and opcao!=2 and opcao !=3:
                print('\033[31mERRO! digite uma opção válida\033[m')
            else:
                break
    if opcao == 3:
        print('-'*40)
        print('Saindo do sistema... Até logo!'.center(40))
        print('-'*40)
        time.sleep(5)
        break
    elif opcao == 2:
        dict.clear()
        nome=input('Nome: ')
        while True:
            idade=input('Idade: ')
            try:
                int(idade)
                break
            except:
                print('\033[31mERRO! digite uma idade válida\033[m')
        print(f'Novo registro de {nome} foi adicionado.')
        dict['nome']=nome
        dict['idade']=idade
        with open('cadastro_total', 'a', encoding='utf-8') as file:
            file.write(f'\n{dict['nome'].ljust(30)} {dict['idade']}')
        time.sleep(2)
    else:
        with open('cadastro_total', 'r', encoding='utf-8') as file:
            conteúdo = file.read()
            print(conteúdo)
        time.sleep(2)