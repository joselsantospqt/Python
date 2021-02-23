import random
import socket
import os

def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func

@rodar
def main():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    print(host)
    porta = 8881
    # Associa a porta
    socket_servidor.bind((host, porta))
    # Escutando...
    socket_servidor.listen()
    while True:
        print("Servidor de nome", host, "esperando conex�o na porta", porta)
        # Aceita alguma conex�o
        (socket_cliente, addr) = socket_servidor.accept()
        print("Conectado a:", str(addr))
        while True:
            msg = socket_cliente.recv(1024)
            # Decodifica mensagem em UTF-8:
            if '$' == msg.decode('utf-8'):
                print("Fechando conexao com", str(addr), "...")
                socket_cliente.close()
                break
            else:
                arquivo = msg.decode('utf-8')
                if os.path.exists(arquivo):
                    caminho_Absoluto = os.getcwd() + "\\"
                    msg = 'Arquivo: ' + arquivo + ' - Encontrado\n'+ 'Tamanho: ' + str(os.stat(caminho_Absoluto + arquivo).st_size)
                else:
                    msg = '-1'

            socket_cliente.send(msg.encode('utf-8'))  # Envia resposta