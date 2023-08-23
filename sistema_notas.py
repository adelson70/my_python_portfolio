# by: adelson70
# SISTEMA DE NOTAS
# funcionalidades
# cadastro de alunos, adiciona notas, calcula media
# imprime alunos acima da media 7 e baixo
#
# somente de uma turma
# https://www.linkedin.com/in/adelson-bittencourt-junior/
banco_dados = {}
from os import system
from time import sleep as pausa

# função que limpa a tela
def limpar_tela():
    system("cls")

while True:
    #banco_dados = {
        #nome_aluno:[[notas],media,situação]
    #}
    opcao_menu = input("""
Digite 1 - Cadastrar Aluno
Digite 2 - Adicionar Notas do Aluno
Digite 3 - Verifica Notas Abaixo da Média
Digite 4 - Verifica Notas Acima da Média
Digite 5 - Imprimir Todos Alunos
Digite 0 - Sair

Digite:  """)

    # variavel lista com todas os numeros de opções do menu
    # sera usada para indicar se a opção é válida ou não
    opcoes_validas = ["0","1","2","3","4","5"]

    # se a opção informada pelo usuario não estiver na lista de opcoes_validas
    if opcao_menu not in opcoes_validas:
        print(f"Opção {opcao_menu.upper()} inválida!")
        pausa(1)
        continue

    # opcao == 0 encerra o programa
    if opcao_menu == "0":
        limpar_tela()
        encerrar = "Encerrando"
        # cria uma animação do encerramento
        for i in range(4):
            print(encerrar)
            encerrar += "."
            pausa(1)
            limpar_tela()
        break
    
    # opcao == 1 ira cadastrar o nome do aluno
    if opcao_menu == "1":
        limpar_tela()
        nome_aluno = input("Digite o nome do aluno: ").upper()

        # se o nome do aluno ja estiver no dicionario banco_dados
        # ficara num loop até digitar um nome não informado anteriormente
        if nome_aluno in banco_dados:
            while nome_aluno in banco_dados:
                limpar_tela()
                print(f"{nome_aluno} já foi cadastrado!")
                nome_aluno = input("Digite outro nome: ").upper()
            # cria uma chave no dicionario banco_dados com o nome do aluno
            banco_dados[nome_aluno] = []
            continue
        # caso o nome seja a primeira vez informado ira adicionar automaticamente no dicionario
        else:
            banco_dados[nome_aluno] = []
            limpar_tela()

    # opcao == 2 cadastra as notas do aluno conforme a quantidade de notas que o usuario informar
    if opcao_menu == "2":
        limpar_tela()

        # se o usuario tentar cadastrar uma nota sem ter cadastrado o nome de um aluno
        # ira retornar uma mensagem
        if banco_dados == {}:
            print("Não existem alunos cadastrados!")
            pausa(1)
            continue
        # printa todos os nomes cadastrados um abaixo do outro
        for nome in banco_dados:
            print(nome)
        nome_aluno_nota = input("Digite o nome do aluno para cadastrar as notas: ").upper()
         
        # se o nome do aluno não estiver no dicionario banco_dados
        # ira ficar num loop até inserir um nome ja cadastrado
        if nome_aluno_nota not in banco_dados:
            while nome_aluno_nota not in banco_dados:
                limpar_tela()
                print("Aluno não encontrado")
                nome_aluno_nota = input("Digite o nome de um aluno cadastrado: ").upper()

        limpar_tela()
        # acessa a area do aluno que ira informar a quantidade de notas e suas
        # respectivas notas
        print(f"Area do Aluno: {nome_aluno_nota.upper()}")
        quantidade_notas = input("Digite a quantidade de notas: ")

        # se o usuario inserir um numero inteiro positivo
        try:
            quantidade_notas = int(quantidade_notas)
            soma = 0
            # lista notas ira adicionar as notas
            # sucessivamente adicionar a lista notas dentro da chave
            notas = []
            for nota in range(quantidade_notas):
                # variavel de ponto flutuante que ira receber a nota
                valor_nota = float(input(f"Digite o valor da nota {nota+1}: "))
                # adiciona a nota na lista notas
                notas.append(valor_nota)
                # soma a nota para futuramente calcular a media
                soma += valor_nota
            # calcula a media do aluno
            media = soma/quantidade_notas
            # condição para dizer se o aluno esta aprovado ou reprovado
            situacao = "Aprovado" if media >= 7 else "Reprovado"

            # adiciona todas as infos acima no dicionario
            banco_dados[nome_aluno_nota] = [notas,media,situacao]

        # se o usuario inserir algo diferente de um numero inteiro positivo
        except ValueError:
            print("Digite apenas numeros inteiros e positivos")
            pausa(1)
            continue
    
    # opcao == 3 ira mostrar os alunos com media abaixo de 7
    # caso o dicionario banco_dados esteja vazio ele
    # ira retornar outra mensagem
    if opcao_menu == "3":
        limpar_tela()

        if banco_dados == {}:
            print("Não existem alunos cadastrados!")
            continue

        print("Alunos Abaixo da Média")
        for chave in banco_dados:
            media_aluno = banco_dados[chave][1]
            if media_aluno < 7:
                print(f"Nome: {chave} Média: {media_aluno}")

    # opcao == 4 ira mostrar os alunos com media acima de 7
    # caso o dicionario banco_dados esteja vazio ele
    # ira retornar outra mensagem
    if opcao_menu == "4":
        limpar_tela()

        if banco_dados == {}:
            print("Não existem alunos cadastrados!")
            continue

        print("Alunos Acima da Média")
        for chave in banco_dados:
            media_aluno = banco_dados[chave][1]
            if media_aluno >= 7:
                print(f"Nome: {chave} Média: {media_aluno}")

    # opcao == 5 ira imprimir todos os alunos cadastrados
    # com seus respectivos valores
    if opcao_menu == "5":
        limpar_tela()

        if banco_dados == {}:
            print("Não existem alunos cadastrados!")
            continue

        for chave in banco_dados:
            print(f"""
--------------------
Nome: {chave}
Notas: {banco_dados[chave][0]}
Média: {banco_dados[chave][1]}
Situação: {banco_dados[chave][2]}""")