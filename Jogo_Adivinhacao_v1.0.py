from random import randint
from time import sleep
import os

#Tela de apresentação
def apresentacao():
    print("*" * 23)
    print("* Jogo da Adivinhação *")
    print("*" * 23)

#Define o número sorteado pela cpu
def cpu_numero():
    numero = randint(0,100)
    return numero

#Escolha de um número feita pelo jogador em um intervalo de 0 até 100.
def jogador_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro de 0 até 100: "))
            if 0 <= numero <= 100:
                return numero
            else:
                print("O número precisa estar no intervalo de 0 a 100. Tente novamente!")
                sleep(2)
        except ValueError:
            print("Você precisa digitar um número inteiro de 0 até 100.\n"
                  "Por favor, tente novamente!")
            sleep(2)
        except:
            print("Ocorreu um erro inesperado.\nPor favor, tente novamente!")
            sleep(2)

#Compara se o número escolhido pelo jogador é igual ao número da cpu.
def comparador(num_cpu, num_jogador):
    global tentativas
    if num_cpu == num_jogador:
        print("CPU: Parabéns! Você acertou!")
        tentativas += 1
        sleep(2)
    elif num_jogador > num_cpu:
        print(f"CPU: O número que estou pensando é menor que {num_jogador}.")
        tentativas += 1
        sleep(1)
    elif num_jogador < num_cpu:
        print(f"CPU: O número que estou pensando é maior que {num_jogador}.")
        tentativas += 1
        sleep(1)

if __name__ == "__main__":
    #Looping que permite com que a pessoa jogue novamente.
    while True:
        os.system('cls')
        apresentacao()
        sleep(2)
        cpu = cpu_numero()
        tentativas = 0
        #Looping que faz o jogo rodar até que o número do jogador seja igual ao da cpu.
        while True:
            palpite = jogador_numero()
            comparador(cpu, palpite)

            if palpite == cpu:
                print(f"Número de tentativas: {tentativas}.")
                sleep(1)
                break
        #Pergunta se o jogador deseja jogar novamente.
        while True:
                jogar_novamente = str(input("Deseja jogar novamente? [S/N]: ")).upper()
                if jogar_novamente == "N":
                    print("Obrigado por jogar! Até a próxima!")
                    sleep(2)
                    exit()
                elif jogar_novamente == "S":
                    break
                else:
                    print("Você precisa digitar 'S' para sim e 'N' para não, apenas.")
                    sleep(2)