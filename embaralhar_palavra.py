# by: adelson70
# linkedin
# https://www.linkedin.com/in/adelson-bittencourt-junior/
# PROGRAMA QUE EMBARALHA UMA PALAVRA
#
def embaralhar(palavra):
    # importar da biblioteca random somente a função choice
    from random import choice
    # variavel lista que sera usada na função choice
    lista_palavra = list(palavra)
    # quantidade de letras que será usado no for para fazer as repetições
    quantidade_letras = len(palavra)
    # variavel que será usada para concatenar a letra aleatoria
    palavra_embaralhada = ""

    # repete de acordo com a quantidade de letras da palavra
    for i in range(quantidade_letras):
        # escolhe randomicamente a letra de acordo com a lista_palavra
        letra_aleatoria = choice(lista_palavra)
        # concatena a varaivel palavra_embaralhada com letra_aleatoria
        palavra_embaralhada += letra_aleatoria
        # remove a letra ultilizada anterioremente
        # remove para não usar letras repetidas
        lista_palavra.remove(letra_aleatoria)
    
    # imprime a palavra embaralhada
    print(palavra_embaralhada)

embaralhar("computador")
