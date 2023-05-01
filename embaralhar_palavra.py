# by: adelson70
# 
# JOGO DA FORCA
# 
# https://www.linkedin.com/in/adelson-bittencourt-junior/

from os import system
from time import sleep as pausa
from string import ascii_lowercase

# função para limpar o terminal usando a biblioteca OS
def limpar_tela():
    system("cls")
limpar_tela()

# função para criar um tempo de execução da linha do código
# usando a biblioteca TIME
# tempo de 1 segundo será o parametro padrão
def esperar(tempo=1):
    pausa(tempo)

# outro usuario ira escolher a palavra secreta e sua respectiva dica
palavra_secreta = input("Digite a palavra secreta: ")
dica = input(f"Digite a dica da palavra {palavra_secreta.upper()}: ")
limpar_tela()

lista_alfabeto = list(ascii_lowercase)
quantidade_letras = len(palavra_secreta)
tentativas = len(palavra_secreta)
palavra = ["-"]*quantidade_letras
letras_utilizadas = []

# enquanto não zerar as tentativas
# tentativas serão igual a quantidade de letras da palavra secreta
while tentativas > 0:
    str_alfabeto = " ".join(lista_alfabeto)
    str_palavra = "".join(palavra)
    limpar_tela()
    print("LETRAS RESTANTES",f"\n{str_alfabeto}")
    print(f"DICA: {dica.upper()}")
    print(str_palavra.upper())
    print("Tentativas:",tentativas)

    # se a palavra for igual a palavra secreta
    # encerra o programa e imprime a mensagem de vitória
    if str_palavra == palavra_secreta:
        limpar_tela()
        print(f"Parabéns você acertou! A palavra era {palavra_secreta.upper()}")
        exit()

    letra = input("Digite uma letra: ").lower()

    if letra == palavra_secreta:
        limpar_tela()
        print(f"Parabéns você acertou! A palavra era {palavra_secreta.upper()}")
        exit()       

    # se o usuario informar mais de 1 letra or não informar nenhuma letra
    if len(letra) > 1 or len(letra) < 1:
        limpar_tela()
        print("Digite apenas uma letra!")
        esperar()
        continue

    # se a letra que o usuario informar não estiver na palavra secreta
    # e não ter sido utilizada anteriormente
    elif letra not in palavra_secreta and letra not in letras_utilizadas:
        limpar_tela()
        print(f"Não tem a letra {letra.upper()}")
        letras_utilizadas.append(letra)
        lista_alfabeto.remove(letra)
        tentativas -= 1
        esperar()
        continue

    # se a letra que o usuario informar ja tiver sido introduzida anteriormente
    elif letra in letras_utilizadas:
        limpar_tela()
        print(f"Letra {letra.upper()} já foi informada!")
        esperar()
        continue

    # se a letra informada pelo usuario estiver na palavra secreta
    elif letra in palavra_secreta:
        limpar_tela()
        letras_utilizadas.append(letra)
        lista_alfabeto.remove(letra)
        # percorre a letra da palavra secreta 
        # até ser igual a letra informada pelo usuario
        # usando enumerate para saber o indice
        for i,l in enumerate(palavra_secreta):
            if letra == l:
                # quando for igual ira substituir o "-" pela letra correspondente
                palavra[i] = letra
        continue

# se as tentativas chegarem a 0 o programa ira imprimir a mensagem de derrota
limpar_tela()
print(f"Você perdeu a palavra era: {palavra_secreta}")
