def jogar():
    print("**********************************")
    print("Bem vindo no jogo de Forca")
    print("**********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    print(type(enforcou))
    print(type(acertou))

    while(not enforcou and not acertou):

        chute = input("Qual Letra?")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra '{letra}' na posição {index}")
                index = index + 1

        print("Jogando...")



if(__name__ == "__main__"):
    jogar()