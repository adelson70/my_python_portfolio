# by: adelson70
#
# CRONOMETRO
# USUARIO IRA INFORMAR O TEMPO EM MINUTOS
# linkedin:
# https://www.linkedin.com/in/adelson-bittencourt-junior/
def timer(tempo):
    # importa da biblioteca sleep somente a função time
    from time import sleep
    # importa da biblioteca os somente a função system
    from os import system

    # função esperar usara a função sleep e o tempo de 1 segundo
    def esperar():
        sleep(1)

    # função limpar_tela ira usar o comando "cls" para limpar o terminal
    def limpar_tela():
        system("cls")
    limpar_tela()

    # minutos é igual ao parametro passado na função timer 
    minutos = tempo
    horas = 0
    segundos = 0
    
    # se os minutos forem mais que 60 firaca preso neste while
    if minutos > 60:
        while (minutos-60) >= 0:
            # toda repetição ira adicionar 1 na variavel horas
            horas += 1
            # toda repetição ira retirar 60 minutos da variavel minutos
            minutos -= 60

    # tempo total em segundos 
    # essa variavel sera usada para verificar quando o loop precisa ser encerrado
    tempo_total_segundos = (minutos*60)+(horas*60*60)+segundos

    # enquanto o tempo total for maior que 0
    while tempo_total_segundos != 0 :
        # se for igual a 0 era encerrar o loop
        if tempo_total_segundos == 0:
            break
        
        # imprime um relogio do seguinte formato HH:MM:SS
        print(f"{horas}:{minutos}:{segundos}")
        # decrementa 1 todo inicio do loop
        tempo_total_segundos -= 1

        # parte do codigo a baixo é o funcionamento do relogio

        # se os segundos fores maiores que 0
        # neste caso os segundos iram decrementar -1 até ser igual 0
        if segundos>0:

            # se o tempo total for menor ou igual 60
            # indicara o ultimo minuto
            if tempo_total_segundos <= 60:
                minutos = 0

            # se os minutos e horas forem igual 0
            # e o tempo total restante for maior que 60 segundos
            # indica que será a ultima hora
            elif minutos == 0 and horas == 0 and tempo_total_segundos > 60:
                minutos = 59
            
            # se os minutos forem igual a 0
            # mas ainda tiver horas
            # significa que terminou uma hora
            if minutos == 0 and horas > 0:
                # adiciona 59 a variavel minutos
                minutos = 59
                # decrementa 1 na variavel horas
                horas -= 1

            # se os minutos forem maior que 0
            # e os segundos forem igual 0 
            # significa o fim de 1 minuto
            elif minutos>0 and segundos == 0:
                minutos -= 1

            segundos -= 1

        # se o segundos forem igual a zero
        # neste caso quando for 0 ira ser atribuido o valor 59 a variavel segundos
        if segundos == 0:
            
            ##############################################################
            # toda esta parte do codigo abaixo é igual ao codigo de cima
            # que esta dentro do bloco if segundos>0:
            if tempo_total_segundos <= 60:
                minutos = 0

            elif minutos == 0 and horas == 0 and tempo_total_segundos > 60:
                minutos = 59
            
            if minutos == 0 and horas > 0:
                minutos = 59
                horas -= 1

            elif minutos>0 and segundos == 0:
                minutos -= 1
            ###############################################################

            segundos = 59

        #print(tempo_total_segundos) - usado apenas para fim de testes
        # espera 1 segundo
        esperar()
        # limpa a tela
        limpar_tela()
    
    #limpa a tela
    limpar_tela()
    # imprime a mensagem de FIM
    # indicando o fim da contagem regressiva
    print("FIM")

tempo = input("Digite o tempo em minutos: ")

# trata se o usuario inserir letras ou numeros decimais
try:
    # para verificar se o usuario inserir apenas numeros inteiros
    # sera feito uma coerção da variavel tempo
    tempo = int(tempo)
    timer(tempo)

# se o usuario inserir uma letra ou numero decimal ira imprimir a mensagem de erro
except ValueError:
    print("Digite apenas numeros inteiros")
