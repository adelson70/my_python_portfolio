# CRIANDO UM PROGRAMA DE ESTOQUE

import pandas as pd
from os import system
from time import sleep

estoque = {
    "cod_item":[],
    "nome":[],
    "quantidade":[],
    "preco":[],
}

def limpar_tela():
    system("cls")
limpar_tela()

def esperar(tempo=2):
    sleep(tempo)

cod_item = 0
def cadastrar_item():
    global cod_item

    nome_item = input("Digite o nome do item a ser cadastrado no estoque: ")
    quantidade_item = int(input(f"Digite a quantidade disponivel do item {nome_item} em estoque: "))
    preco_item = float(input(f"Digite o preço do item {nome_item}: "))

    estoque["cod_item"].append(cod_item)
    estoque["nome"].append(nome_item)
    estoque["quantidade"].append(quantidade_item)
    estoque["preco"].append(preco_item)

    cod_item += 1

    print(f"O item {nome_item} foi cadastrado com sucesso!")
    esperar()

def alterar_nome_item():
    cod_item_buscar = int(input("Digite o código do item a ser alterado o nome: "))

    if cod_item_buscar not in estoque["cod_item"]:
        limpar_tela()
        print(f"o código {cod_item_buscar} não foi encontrado!")
        esperar()

    else:
        nome_atual = estoque["nome"][cod_item_buscar]
        novo_nome = input("Digite o novo nome do item: ")
        limpar_tela()
        print(f"Item {nome_atual} foi alterado para {novo_nome}!")
        estoque["nome"][cod_item_buscar] = novo_nome
        esperar()

def incrementar_quantidade():
    cod_item_buscar = int(input("Digite o código do item a ser incrementado a quantidade: "))

    if cod_item_buscar not in estoque["cod_item"]:
        limpar_tela()
        print(f"o código {cod_item_buscar} não foi encontrado!")
        esperar()

    else:
        nome_item = estoque["nome"][cod_item_buscar]

        quantidade_incrementada = int(input(f"Digite a quantidade a ser adicionada no estoque do item {nome_item}: "))

        estoque["quantidade"][cod_item_buscar] += quantidade_incrementada
        print(f"Foi adicionado {quantidade_incrementada} unidades do item {nome_item}!")
        esperar()

def decrementar_quantidade():
    cod_item_buscar = int(input("Digite o código do item a ser decrementado a quantidade: "))

    if cod_item_buscar not in estoque["cod_item"]:
        limpar_tela()
        print(f"o código {cod_item_buscar} não foi encontrado!")
        esperar()

    else:
        nome_item = estoque["nome"][cod_item_buscar]

        quantidade_decrementada = int(input(f"Digite a quantidade a ser removida no estoque do item {nome_item}: "))

        if quantidade_decrementada > estoque["quantidade"][cod_item_buscar]:
            limpar_tela()
            print(f"Estoque do item {nome_item} não possui {quantidade_decrementada} unidades para ser retirada!")
            
        else:
            estoque["quantidade"][cod_item_buscar] -= quantidade_decrementada
            print(f"Foi removido {quantidade_decrementada} unidades do item {nome_item}")

def alterar_preco_item():
    cod_item_buscar = int(input("Digite o código do item a ser alterado o preço: "))

    if cod_item_buscar not in estoque["cod_item"]:
        limpar_tela()
        print(f"O código {cod_item_buscar} não foi encontrado!")
        esperar()

    else:
        preco_atual = estoque["preco"][cod_item_buscar]
        nome_item = estoque["nome"][cod_item_buscar]

        novo_preco = float(input(f"Digite o novo preço do item {nome_item}: "))

        estoque["preco"][cod_item_buscar] = novo_preco

        print(f"Preço do item {nome_item} foi atualizado para R$ {novo_preco}!")
        esperar()

def visualizar_em_tabela(banco_dados=estoque):
    df = pd.DataFrame(banco_dados)
    print(df)
    esperar(10)

def salvar_dados_em_excel(banco_dados=estoque):
    df = pd.DataFrame(banco_dados)
    df.to_excel("Estoque.xlsx",index=False)
    print("Estoque foi salvo numa planilha do excel!")
    esperar()

while True:
    limpar_tela()
    opcoes_validas = ["C","N","I","D","P","V","S","Q"]
    vazio = True if len(estoque["cod_item"]) == 0 else False

    opcao = input("""
[C] - Cadastrar Item no Estoque
[N] - Alterar Nome do Item em Estoque
[I] - Incrementar Qtd Item em Estoque
[D] - Decremetnar Qtd Item em Estoque
[P] - ALterar Preço do Item em Estoque
[V] - Visualizar Itens em Estoque
[S] - Salvar Estoque num Arquivo xlsx
[Q] - Encerrar Programa

Digite => """).upper()
    
    if opcao not in opcoes_validas:
        limpar_tela()
        print("Opção Inválida!")
        esperar()

    elif opcao == "C":
        limpar_tela()
        cadastrar_item()
        esperar()

    elif vazio:
        limpar_tela()
        print("Cadastre um Item no Estoque Primeiro!")
        esperar()

    elif opcao == "N":
        limpar_tela()
        alterar_nome_item()
        esperar()

    elif opcao == "I":
        limpar_tela()
        incrementar_quantidade()
        esperar()

    elif opcao == "D":
        limpar_tela()
        decrementar_quantidade()
        esperar()

    elif opcao == "P":
        limpar_tela()
        alterar_preco_item()
        esperar()

    elif opcao == "V":
        limpar_tela()
        visualizar_em_tabela()
        esperar()

    elif opcao == "S":
        limpar_tela()
        salvar_dados_em_excel()
        esperar()

    elif opcao == "Q":
        limpar_tela()
        print("Encerrando...")
        esperar()
        break