import random

print("**********************************")
print("Bem vindo no jogo de Adivinhação")
print("**********************************")

#numero_int = int(random.random() * 100)
numero_secreto = random.randrange(1, 101)
#numero_secreto = round(random.random() * 100)
total_de_tentativas = 0
pontos = 1000

print("QUal nível de dificuldade ?", numero_secreto)
print("(1) fácil ,(2) médio, (3) difícil")

nivel = int(input("Defina o nível: "))


if(nivel == 1):
    total_de_tentativas = 20

elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100 !")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("você acertou e fez {} pontos !".format(pontos))
        break
    else:
        if (maior):
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Você errou pra maior")

        elif (menor):
            print("Você errou pra menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



print("**********************************")
print("Teste de Calculo")
print("**********************************")
pontos_perdidos = abs(21 - 32) / 3
print("normal     ")
print(pontos_perdidos)
print("arredondado")
print(round(pontos_perdidos))
