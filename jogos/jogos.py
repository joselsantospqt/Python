import forca
import sistema2


def escolhe_jogo():
    print("**********************************")
    print("Escolhe seu jogo")
    print("**********************************")
    print("(1) Forca ,(2) Adivinhação")

    jogo = int(input("Qual Jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação")
        sistema2.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()