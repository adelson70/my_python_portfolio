# github: adelson70
#
# SORTEADOR DE NÚMEROS
#
# linkedin: https://www.linkedin.com/in/adelson-bittencourt-junior/
#
from os import system
from time import sleep
from random import sample

def esperar(tempo=2): # FUNÇÃO DE TEMPO DE ESPERA PARA PROXIMA LINHA DE CODIGO
    sleep(tempo)

def limpar_tela(): # FUNÇÃO PARA LIMPAR A TELA DO TERMINAL
    system("cls")
limpar_tela()

def encerrar_programa(): # FUNÇÃO QUE IRA IMPRIMIR A MSG DE ENCERRAMENTO DO PROGRAMA
    msg = "Encerrando"
    for i in range(4):
        limpar_tela()
        print(msg)
        esperar()
        msg += "."
    exit()

# USUARIO IRA DECIDIR O RANGE INICIAL E FINAL, ONDE OS NÚMEROS SERÃO SORTEADOS
numero_inicial_range = int(input("Digite o número inicial do range: "))
numero_final_range = int(input("Digite o número final do range: "))
limpar_tela()

# CRIA UMA LISTA DE NÚMEROS CONFORME INFORMADO O RANGE PELO USUARIO
# CRIA A LISTA USANDO LIST COMPREHENSION
numeros = [n for n in range(numero_inicial_range,numero_final_range+1)]

# LISTA ONDE SERÃO ARMAZENADOS OS NÚMEROS SORTEADOS
numeros_sorteados = []

def sortear_numero():
    global numeros
    global numeros_sorteados
    numero_sorteado = sample(numeros,1) # ESCOLHE UM NUMERO ALEATORIO DA LISTA DE NUMEROS GERADOS
    numero_sorteado = numero_sorteado[0] # TRANSFORMA DE LISTA PARA APENAS O NUMERO INTEIRO
    numeros.remove(numero_sorteado) # REMOVE O NUMERO SORTEADO DA LISTA DE NUMEROS GERADOS
    numeros_sorteados.append(numero_sorteado) # ADD O NUMERO SORTEADO NA LISTA DE NUMEROS SORTEADOS
    print(f"Número Sorteado: {numero_sorteado}") # IMPRIME O NUMERO SORTEADO AO USUARIO

# MENU ONDE OCORRERA O LOOP DE EXECUÇÃO DO PROGRAMA
while True:
    limpar_tela()
    opcao = input(f"""
Números Sorteados: {numeros_sorteados}

[1] - Sortear Número
[0] - Sair

Digite => """)
    
    opcoes_validas = ["0","1"] # SERA USADO PARA TRATAR A ENTRADA DE OPÇÕES INVALIDAS

    if opcao not in opcoes_validas:
        limpar_tela()
        print("Opção Inválida!")
        esperar()

    elif opcao == "0":
        limpar_tela()
        encerrar_programa()

    elif opcao == "1":
        limpar_tela()
        sortear_numero()
        esperar()