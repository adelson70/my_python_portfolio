# CALCULADORA DE NPS - NET PROMOTER SCORE
# ESCALA DE 0 A 10
# ADICIONA AS RESPOSTAS
# E CALCULA O SCORE
# linkedin: https://www.linkedin.com/in/adelson-bittencourt-junior/

# IMPORTANDO 2 BIBLIOTECAS PARA CRIAR FUNÇÕES POSTERIORES
from os import system
from time import sleep

# VARIAVEL DICIONARIO QUE SERA USADA PARA ARMAZENAR AS RESPOSTAS
escala = {
    "Promotores":0,
    "Neutros":0,
    "Detratores":0,
    "Total de Respostas":0
}

# FUNÇÃO DE LIMPAR O CONSOLE USANDO A BIBLIOTECA SYSTEM
def limpar_console():
    system("cls")
limpar_console()

# FUNÇÃO DE TEMPO DE ESPERA PARA PROXIMA LINHA DE CÓDIGO USANDO A BIBLIOTECA SLEEP
def esperar(tempo=2):
    sleep(tempo)

# FUNÇÃO PARA ADICIONAR UM CLIENTE PROMOTOR NO DICIONARIO
# INCREMENTA +1 NOS CLIENTES PROMOTORES E NO TOTAL DE RESPOSTAS
def add_cliente_promotor(dados = escala):
    dados["Promotores"] += 1 
    dados["Total de Respostas"] += 1
    print("Obrigado pela sua opinião :D") 

# FUNÇÃO PARA ADICIONAR UM CLIENTE NEUTRO NO DICIONARIO
# INCREMENTA +1 NOS CLIENTES NEUTROS E NO TOTAL DE RESPOSTAS
def add_cliente_neutro(dados = escala):
    dados["Neutros"] += 1
    dados["Total de Respostas"] += 1
    print("Obrigado pela sua opinião :D")

# FUNÇÃO PARA ADICIONAR UM CLIENTE DETRATOR NO DICIONARIO
# INCREMENTA +1 NOS CLIENTES DETRATORES E NO TOTAL DE RESPOSTAS
def add_cliente_detrator(dados = escala):
    dados["Detratores"] += 1
    dados["Total de Respostas"] += 1
    print("Obrigado pela sua opinião :D")

# FUNÇÃO PARA CALCULAR O NPS
# AQUI QUE A MAGIA ACONTECE
def calcular_nps():
    # FORMULA DO NPS
    nps = int(((escala["Promotores"]-escala["Detratores"])/escala["Total de Respostas"])*100)

# CONDIÇÕES QUE SÃO OS CRITERIOS DE ACORDO COM CADA PONTUAÇÃO DO SCORE

    if nps >= 91:
        print(f"Score: {nps}")
        print("Parabéns seu Score esta na Zona de Encantamento!")

    elif nps <= 90 and nps >= 76:
        print(f"Score: {nps}")
        print("Parabéns seu Score esta na Zona de Excelência!")
    
    elif nps <= 75 and nps >= 51:
        print(f"Score: {nps}")
        print("Parabéns seu Score esta na Zona de Qualidade!")
    
    elif nps <= 50 and nps >= 1:
        print(f"Score: {nps}")
        print("Seu Score esta na Zona de Aperfeiçoamento!")

    else:
        print(f"Score: {nps}")
        print("Cuidado! seu Score esta na Zona Crítica!")

# FUNÇÃO PARA INSERIR A NOTA DO USUARIO, SERA TRATADA CASO SEJA UMA STRING OU NUMERO INCOMPATIVEL
def avaliar_nota():
    while True:
        # USANDO TRY E EXCEPT PARA TRATAR O ERRO DE VALOR, PARA O CASO DO USUARIO INSERIR UMA STR
        try:
            limpar_console()
            nota = int(input("Digite uma nota de 0 a 10: "))
            # SE A NOTA FOR FORA DA ESCALA DE SATISFAÇÃO
            if nota < 0 or nota > 10:
                limpar_console()
                print("Nota tem quer ser de 0 a 10!")
                esperar()
                continue

            else:
                return nota
        # SE A ENTRADA DO USUARIO CONTER LETRAS
        except ValueError:
            limpar_console()
            print("Digite apenas números inteiros! De 0 a 10")
            esperar()

while True:
    limpar_console()
    menu = input("""
[S] - Escala de Satisfação                
[R] - Resultado
                 
Digite : """).upper()
    
    if menu == "S":
        limpar_console()
        nota = avaliar_nota()

        if nota >= 0 and nota <= 6:
            limpar_console()
            add_cliente_detrator()
            esperar()

        elif nota >= 7 and nota <= 8:
            limpar_console()
            add_cliente_neutro()
            esperar()

        elif nota >= 9 and nota <= 10:
            limpar_console()
            add_cliente_promotor()
            esperar()

    elif menu == "R":
        limpar_console()

        # CASO O USUARIO PEÇA UM RESULTADO MAS O DICIONARIO ESTEJA VAZIO
        if escala["Total de Respostas"] == 0:
            limpar_console()
            print("Sem Dados para Calcular!")
            esperar()
            continue

        calcular_nps()
        esperar()

    
    # elif menu == "I":
    #     print(escala)
    #     esperar(5)

    else:
        limpar_console()
        print("Opção Inválida!")
        esperar()