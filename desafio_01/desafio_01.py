'''Desafio 01'''

saldo = 0.0
limite_saque = 500.0
extrato = ""

numero_saques_dia = 0
NUMERO_LIMITE_SAQUES_DIARIO = 3

MENU = '''
    ---------------------------
            Operações
    ---------------------------

    (1) - Depósito
    (2) - Saque
    (3) - Extrato (saldo)

    (0) - Sair

    --------------------------------
    Digite a opção desejada [0-3]: '''

while True:

    opcao = input(MENU)
    opcao = -99 if not opcao.isnumeric() else int(opcao)

    bln_espera = False

    if opcao == 0:
        break

    elif opcao == 1:

        deposito = -1.

        while deposito < 0:
            valor_digitado = input('\n    Depósito\n    - Digite o valor (0 para sair): ')
            # TODO: Aplicar um tratamento de erro para valores não númericos.
            deposito = float(valor_digitado)
            if deposito < 0:
                print('\n    *** O valor de depósito deve ser númerico  e igual ou superior a 0')

        if deposito >0:
            saldo += deposito
            extrato += f'    Depósito: R$ {deposito:10.2f} (+)\n'
       
    elif opcao == 2:

        if numero_saques_dia == NUMERO_LIMITE_SAQUES_DIARIO:
            print('\n   ',"."*41)
            print('    | Operação não permitida:               |')
            print(f'    | Acima do limite diário de saques ({NUMERO_LIMITE_SAQUES_DIARIO}). |')
            print('   ',"."*41)

            bln_espera = True

        elif saldo == 0:
            print('\n','  ',"."*27)
            print('    | Operação não permitida: |')
            print('    | Saldo igual a R$ 0,00.  |')
            print('   ',"."*27)
            
            bln_espera = True

        else:
            saque = -1.

            while (saque < 0 or saque > limite_saque or saque > saldo) and numero_saques_dia < NUMERO_LIMITE_SAQUES_DIARIO:
                valor_digitado = input(f'\n    Saque ({numero_saques_dia+1}/{NUMERO_LIMITE_SAQUES_DIARIO})\n    - Digite o valor (0 para sair): ')
                # TODO: Aplicar um tratamento de erro para valores não númericos.
                saque = float(valor_digitado)
                if saque < 0:
                    print('\n    *** O valor de saque deve ser igual ou superior a: R$ 0,00')
                elif saque > limite_saque:
                    print(f'\n    *** O valor de saque deve ser inferior ao limite (R$ {limite_saque:0.2f})')
                elif saque > saldo:
                    print(f'\n    *** O valor de saque deve ser inferior ao saldo (R$ {saldo:0.2f})')

            if saque > 0:
                saldo -= saque
                extrato += f'    Saque   : R$ {saque:10.2f} (-)\n'
                numero_saques_dia += 1

    elif opcao == 3:

        print('\n',' '*2,' Extrato '.center(27,'-'),'\n')
        
        if extrato:
            print(extrato)
            print('\n   ','-'*27)
            print(f'    Saldo   : R$ {saldo:10.2f} (=)\n')
        
        else:
            print('    *** Sem operações até o momento. ***')
            
        bln_espera = True

    else:
        print('\n   ',"."*53)
        print('    | Operação inválida, selecione a operação desejada. |')
        print('   ',"."*53)
        
        bln_espera = True

    
    if bln_espera:
        input('\n\n    Tecle [Enter]: ')
