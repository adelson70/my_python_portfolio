from time import sleep
from os import system

def limpar_tela(): # função para limpar tela usando a biblioteca os
    system("cls")

def esperar(tempo=3): # função para criar uma espera para avançar para proxima linha de codigo
    sleep(tempo) # usando a função time da biblioteca time

# função criada para verificar se um numero é inteiro e positivo
numero_inteiro_positivo = True
def verifica_numero_inteiro_positivo(numero):
    global numero_inteiro_positivo # ira atribuir valores a variavel que esta fora do escopo da função

    numero_inteiro_positivo = True
    try:# tentara converter a string em int se der certo ira fazer uma verificação condicional
        numero = int(numero)
        if numero <= 0:
            numero_inteiro_positivo = False

    except ValueError:# se não conseguir converter a string em int, significa que tem letras na string
        numero_inteiro_positivo = False

# função criada para verificar se a string é um número
e_numero = True
def verifica_se_e_numero(numero):
    global e_numero # ira atribuir valores a variavel que esta fora do escopo da função
    try:# tentara converter a string em float se der certo ira fazer uma verificação condicional
        numero = float(numero)
        e_numero = True

    except ValueError:# se não conseguir converter a string em float, significa que tem letras na string
        e_numero = False

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# loop infinito onde ocorrera todo codigo do programa
while True:
    limpar_tela()
    print(f"Saldo Atual R$ {saldo:.2f}") # imprime uma mensagem do saldo atual
    opcao = input(menu) # imprime o menu podendo entrar com dados do teclado

    # bloco de codigo que fara o deposito na conta bancaria
    if opcao == "d":
        limpar_tela()
        valor_deposito = input("Digite um valor de deposito que seja um numero inteiro: ")
        verifica_numero_inteiro_positivo(valor_deposito)

        while numero_inteiro_positivo == False: # enquando o usuario não informar um numero valido
            limpar_tela()
            print("Digite um número inteiro positivo!")
            valor_deposito = input("Digite um valor de deposito que seja um numero inteiro: ")
            verifica_numero_inteiro_positivo(valor_deposito)
        
        valor_deposito = int(valor_deposito)
        
        limpar_tela()
        print(f"Você Depositou R$ {valor_deposito:.2f}")
        esperar()
        extrato += f"Deposito: R$ {valor_deposito:.2f}-"
        saldo += valor_deposito
        continue

    # bloco de codigo que fara o saque da conta bancaria
    elif opcao == "s":
        numero_saques += 1
        limpar_tela()

        if saldo == 0:
            print(f"Seu saldo é de R$ {saldo:.2f}")
            esperar()
            continue

        if numero_saques > 3:
            print("Você atingiu seu limite de saque diario!")
            esperar()
            limpar_tela()
            continue

        valor_saque = input("Digite um valor a ser sacado: ")
        verifica_se_e_numero(valor_saque)
        
        while e_numero == False: # enquando o usuario não informar um numero
            limpar_tela()
            print("Digite apenas números!")
            valor_saque = input("Digite um valor a ser sacado: ")
            verifica_se_e_numero(valor_saque)
            limpar_tela()

        valor_saque = float(valor_saque)
        if valor_saque > 500:
            print(f"Seu limite de saque por operação é de R$ {limite}")
            esperar()
            limpar_tela()
            continue

        if valor_saque > saldo:
            print(f"Seu saldo é de R$ {saldo:.2f}")
            print(f"Valor de saque solicitado foi maior que seu saldo!")
            esperar()
            continue

        else:
            limpar_tela()
            print(f"Você sacou R$ {valor_saque:.2f}")
            extrato += f"Saque: R$ {valor_saque:.2f}-"
            saldo -= valor_saque     

    # bloco de codigo que ira imprimir o extrato da conta bancaria
    elif opcao == "e":
        limpar_tela()

        for i in extrato:
            if i == "-":
                print("\n")
            else:
                print(i,end="")

        print(f"Saldo Atual: R$ {saldo:.2f}")
        esperar(10)

    # bloco de codigo que ira encerrar o loop
    elif opcao == "q":
        limpar_tela()
        print("Encerrando")
        esperar()
        break
    
    # bloco de codigo que ira informar se o usuario entrou com algum comando invalido ao menu
    else:
        limpar_tela()
        print("Comando Invalido!")
        esperar()
        continue
