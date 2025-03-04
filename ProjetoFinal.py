menu = """

------------------- Banco Uni DIO -------------------
\n
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
\n
-----------------------------------------------------

=> """

saldo = 0 
limite = 500
extrato = {'D' : {0:0},
           'S' : {0:0}}
numero_saques = 0
LIMITES_SAQUES = 3


def menu1():
    menu1 = """
            ----------------------
            [1] Sim
            [2] Não
            ----------------------
            """
    print(menu1)

    
while True:

    opcao = input(menu)

    if opcao == '1':
        print("Depósito")
        D = int(input('\nDigite o valor que deseja depositar: '))
        if D <= 0:
            print('\nOperação Cancelada. O valor a ser depositado é negativo!')
            
        elif D > 0:
            print(f'Deseja depositar o valor de R${D}?')
            menu1()
            opcao2 = input(menu1)
            if opcao2 == '1':
                print('\nDepósito está sendo processado.')
                saldo += D
                extrato['D'][len(extrato['D'])] = D
                print(f'\nO valor {D} foi depositado com sucesso!')
            elif opcao2 == '2':
                print('Operação Cancelada!')



    elif opcao == '2':
        print("Saque")
        S = int(input('\nDigite o valor que deseja sacar?'))
        if S <= 500 and saldo >= S and numero_saques < LIMITES_SAQUES:
            print(f'\nDeseja mesmo sacar {S} ?')
            menu1()
            opcao3 = input(menu1)
            if opcao3 == '1':
                print('\nAguarde. O saque está sendo efetuado.')
                saldo -= S
                extrato['S'][len(extrato['S'])] = S
                numero_saques += 1
                print('\nSaque efetuado com sucesso!')
            elif opcao3 == '2':
                print('\nOperação Cancelada!')
        elif S > 500:
            print('\nO valor de saque requerido é maior que o permitido. ')
        elif saldo < S:
            print('\nSaldo insuficiente!')
        elif numero_saques >= LIMITES_SAQUES:
            print('\nLimites de saques diários atingido.')


    elif opcao == '3':
        print("\nExtrato")
        print('\nDepósitos')
        for i in range(1,len(extrato['D'])):
            print(f'R${extrato['D'][i]}')

        print('\nSaques')
        for i in range(1,len(extrato['S'])):
            print(f'- R${extrato['S'][i]}')

        print(f'\nSaldo Atual: R$ {saldo}')


    elif opcao == '4':
        break

    else:
        print('Operação inválida, por favor selecione uma operação desejada. ')
