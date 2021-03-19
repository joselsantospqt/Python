import os
import pickle
import socket

# Cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 8881
tcp.bind((host, porta))
tcp.listen()

(socket_cliente, addr) = tcp.accept()
print("Conectado a:", str(addr))

response = []
while True:
    mensagem = socket_cliente.recv(4096)
    getDiretorio = mensagem.decode('UTF-8')

    if getDiretorio != 'fim':
        for arquivo in os.listdir(getDiretorio):
            if os.path.isfile(getDiretorio + '//' + arquivo):
                response.append(arquivo)

        bytes = pickle.dumps(response)
        socket_cliente.send(bytes)

    else:
        break

socket_cliente.close()

input("Pressione qualquer tecla para sair...")