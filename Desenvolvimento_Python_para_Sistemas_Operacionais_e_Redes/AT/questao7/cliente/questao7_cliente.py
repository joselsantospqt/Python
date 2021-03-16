import os
import socket, time

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 8881))

    nome_arquivo = input('Escreva o nome do arquivo')
    s.send(nome_arquivo)

    pathLocal = os.environ["IDE_PROJECT_ROOTS"]
    tamanho = int(s.recv(10).decode('utf-8'))
    if tamanho >= 0:
        recebido = s.recv(tamanho)
        caminho = f'{pathLocal}/AT/questao6/cliente/{nome_arquivo}'
        local = open(caminho, 'wb')
        local.write(recebido)
        local.close()
    else:
        print('não existe arquivo no servidor')

except Exception as erro:
    print(str(erro))

# Fecha o socket
s.close()

input("Pressione qualquer tecla para sair...")