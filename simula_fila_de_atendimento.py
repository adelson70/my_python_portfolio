# by: adelson70
#
# FILA DE ATENDIMENTO
# USUARIO IRA CRIAR UMA FILA DE ATENDIMENTO, ACRESCENTANDO NOVAS PESSOAS
# E ATENDENDO SEMPRE A PRIMEIRA PESSOA DA FILA
# linkedin:
# https://www.linkedin.com/in/adelson-bittencourt-junior/

from os import system
from time import sleep

def limpar_tela():# função para limpar a tela do console
    system("cls")

def esperar(tempo=3):# função para criar uma pausa de 3seg para proxima linha de cod
    sleep(tempo)

lista_fila = []# variavel lista onde serão armazenados os nomes

def atender_pessoa_fila(fila=lista_fila):# função para remover a pessoa da lista de pessoas
    pessoa_atendida = fila[0]# identifica a primeira pessoa da fila pelo indice 0
    limpar_tela()
    print(f"{pessoa_atendida} foi atendido!")
    fila.pop(0)
    esperar()

def nova_pessoa_fila(pessoa,fila=lista_fila):# função para adicionar uma nova pessoa na lista
    fila.append(pessoa)
    ultima_pessoa = fila[-1]# identifica a ultima pessoa da fila pelo indice -1
    limpar_tela()
    print(f"{ultima_pessoa} é a última pessoa da fila!")
    esperar()

while True:# loop onde ocorrerá todo funcionamento
    limpar_tela()
    fila = ", ".join(lista_fila)# transforma a lista em string para ficar mais bonito no print
    vazio = True if len(lista_fila) == 0 else False# verificação para averiguar se tem alguem na fila

    limpar_tela()
    print(f"Pessoas na Fila: {fila}")
    
    if vazio != True:# se tiver alguem na fila printará este menu
        comando = input(f"""
[a] - Atender {lista_fila[0]}
[p] - Adicionar uma Pessoa na Fila

=> """)
        if comando == "a":# comando "a" ira chamar a função de atender uma pessoa
            atender_pessoa_fila()            

        elif comando == "p":# comando "p" ira chamar a função de add nova pessoa na fila
            limpar_tela()
            nome = input("Digite o nome da nova pessoa: ").capitalize()
            nova_pessoa_fila(nome)

        else:# se nenhum dos comandos acima, imprimi uma msg de erro
            limpar_tela()
            print("Comando Invalido!")
            esperar()

    else:# se a fila de pessoas estiver vazia, ira printar este menu abaixo
        limpar_tela()
        comando = input("""
Fila Vazia

[p] - Adicionar uma Pessoa na Fila

=> """)
        if comando == "p":# comando "p" ira chamar a função de adicionar uma pessoa
            limpar_tela()
            nome = input("Digite o nome da nova pessoa: ").capitalize()
            nova_pessoa_fila(nome)

        else:# se o comando for diferente ira aparecer esta msg de erro
            limpar_tela()
            print("Comando Inválido!")
            esperar()