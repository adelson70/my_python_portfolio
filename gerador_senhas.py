# by: adelson70
#
# GERADOR DE SENHA
# gera uma senha de 12 caracteres
# armazena as senhas geradas num bloco de notas de nome "senhas"
# 3 letras minusculas, 3 letras maiusculas, 3 numeros, 3 simbolos
# usuario podera passar o parametro de quantidade de senhas (opcional)
# linkedin:
# https://www.linkedin.com/in/adelson-bittencourt-junior/

# parametro quantidade_senhas por padrão será 1
# mas o usuario podera alterar para imprimir a quantidade de senhas desejaveis
def gerar_senha(quantidade_senhas=1):
    # importa a biblioteca random, string e sistema operacional
    import random
    import string
    from os import system

    # cria um arquivo txt que sera gravado todas as senhas geradas
    arquivo_senhas = open("senhas.txt","w")

    # função para limpar o terminal
    def limpar_tela():
        system("cls")
    limpar_tela()

    # cria a variavel lista lista_senha
    # que sera usada pra adicionar os caracteres aleatorios da senha
    lista_senha = []
    # usando a biblioteca string cria uma variavel que contenha as letras do alfabeto em minusculo
    alfabeto_minusculo = string.ascii_lowercase
    # usando a biblioteca string cria uma variavel que contenha as letras do alfabeto em maiusculo
    alfabeto_maiusculo = string.ascii_uppercase
    # variavel com todos os numeros
    numeros = "0123456789"
    # variavel com alguns caracteres especiais
    especiais = "!@#$%&*?_-"

    for i in range(quantidade_senhas):
        # limpa a lista no inicio de cada nova senha
        lista_senha.clear()
        # laço de repetiçao de 3 vezes
        for c in range(3):
            # dentro deste for usando a biblioteca random e a função choice
            # a função choice escolhera aleatoriamente dentro da string de letras, numeros e especiais
            # se houver algum caracter repetido o programa escolherá outro caracter
            letra_minuscula = random.choice(alfabeto_minusculo)
            while letra_minuscula in lista_senha:
                letra_minuscula = random.choice(alfabeto_minusculo)

            letra_maiuscula = random.choice(alfabeto_maiusculo)
            while letra_maiuscula in lista_senha:
                letra_maiuscula = random.choice(alfabeto_maiusculo)

            numero = random.choice(numeros)
            while numero in lista_senha:
                numero = random.choice(numeros)

            especial = random.choice(especiais)
            while especial in lista_senha:
                especial = random.choice(especiais)

            # quando todos caracteres forem escolhidos e não forem repetidos
            # sera adicionado os 4 caracteres na lista_senha

            lista_senha.append(letra_minuscula)
            lista_senha.append(letra_maiuscula)
            lista_senha.append(numero)
            lista_senha.append(especial)

        # função shuffle embaralha os elementos dentro da lista_senha
        random.shuffle(lista_senha)
        # transforma a lista_senha numa string e coloca este valor na variavel string_senha
        string_senha = "".join(lista_senha)
        # imprime a senha gerada com sucesso!
        
        # se o usuario pedir somente 1 senha
        # a senha gerada ira aparecer no terminal
        if quantidade_senhas == 1:
            continue

        # se for mais que 1 senha
        # a senha gerada ira ser escrita numa linha do arquivo txt
        else:
            # metodo write para escrever no bloco de notas a senha e inserir uma quebra de linha no final
            arquivo_senhas.write(f"{string_senha}\n")
    
    # imprime esta mensagem de for somente 1 senha
    if quantidade_senhas == 1:
        print("Senha Gerada com Sucesso!")
        print(string_senha)

    # imprime esta mensagem se for mais de 1 senha
    else:
        print(f"{quantidade_senhas} Senhas Geradas com Sucesso!")

    # ao final do loop sera encerrado o arquivo para não haver problemas com o SO da maquina
    arquivo_senhas.close()

quantidade_senhas = int(input("Digite a quantidade de senhas a ser gerado: "))
gerar_senha(quantidade_senhas)
