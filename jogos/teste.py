numero_secreto = 42
chute_str = input("Digite o seu numero: ")
chute = int(chute_str)

acertou = (chute == numero_secreto)

print(acertou)

if acertou:
    print("Parabéns! Você acertou.")
else:
    print("Parabéns! Você ERROU ! kk.")

    nome = "Nico"
    sobrenome = "Steppat"
    print(nome, sobrenome, sep="_")
