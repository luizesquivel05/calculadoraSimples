import os
import time

# dicionario das opções:
contas = dict()
contas['0'] = "soma"
contas['1'] = "subtração"
contas['2'] = "produto"
contas['3'] = "divisão"
contas['4'] = "porcentagem"

# impressao das opções e menu:
while True:
    print('''
        Olá, caro usuário de nossa Calculadora, podemos começar?
        
        Digite S para sim e N para não
    ''')
    time.sleep(2)
    if str(input()) == "N": break
    os.system('cls')
    print('''
        ----------------------------------------------------------
        Então, vamos dar continuidade.
        ----------------------------------------------------------
        0 - somar (A + B)
        1 - subtração (A - B)
        2 - produto (A * B)
        3 - divisão (A / B)
        4 - porcentagem (A % B)
        ----------------------------------------------------------
    ''')
    opcao = int(input('Digite sua opção entre 0 e 4: '))
    while opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        opcao = int(input('Digite sua opção entre 0 e 4: '))
    else:
        if opcao == 0:
            A = int(input('Digite o primeiro valor: '))
            B = int(input('Digite o segundo valor: '))
            time.sleep(2)
            os.system('cls')
            print(f'O cálculo foi realizado: \n\n {A} + {B} = {A+B}')
        elif opcao == 1:
            A = int(input('Digite o primeiro valor: '))
            B = int(input('Digite o segundo valor: '))
            time.sleep(2)
            os.system('cls')
            print(f'O cálculo foi realizado: \n\n {A} + {B} = {A-B}')
        elif opcao == 2:
            A = int(input('Digite o primeiro valor: '))
            B = int(input('Digite o segundo valor: '))
            time.sleep(2)
            os.system('cls')
            print(f'O cálculo foi realizado: \n\n {A} + {B} = {A*B}')
        elif opcao == 3:
            A = int(input('Digite o primeiro valor: '))
            B = int(input('Digite o segundo valor: '))
            time.sleep(2)
            os.system('cls')
            print(f'O cálculo foi realizado: \n\n {A} + {B} = {A/B}')
        elif opcao == 4:
            A = int(input('Digite o primeiro valor: '))
            B = int(input('Digite o segundo valor: '))
            time.sleep(2)
            os.system('cls')
            print(f'O cálculo foi realizado: \n\n {A} + {B} = {A%B}')
    time.sleep(10)
    print('''
        Olá, caro usuário de nossa Calculadora, deseja continuar?
        
        Digite S para sim e N para não.
    ''')
    time.sleep(2)
    if str(input()) == "N": break
    os.system('cls')