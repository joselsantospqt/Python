import os
import pickle
import socket, time

# Cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    tcp.connect((socket.gethostname(), 8881))

    mensagem = input('Escreva o nome do caminho: ')
    tcp.send(mensagem.encode('UTF-8'))

    bytes = tcp.recv(4096)
    retorno = pickle.loads(bytes)

    for item in retorno:
        print(item)

    mensagem = 'fim'
    tcp.send(mensagem.encode('UTF-8'))

except Exception as erro:
    print(str(erro))

# Fecha o socket
tcp.close()

input("Pressione qualquer tecla para sair...")