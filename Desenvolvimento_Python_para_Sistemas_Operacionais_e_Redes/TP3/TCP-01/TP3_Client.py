import socket
import sys

def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func

@rodar
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Tenta se conectar ao servidor
        s.connect(("rico-pc", 8881))
    except Exception as erro:
        print(str(erro))
        sys.exit(1)  # Termina o programa
    print("Escreva o nome do arquivo:\n")
    msg = input()
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
    while msg != '$':
        msg = s.recv(1024)
        print(msg.decode('utf-8'))
        msg = input("Para encerrar, digite '$'\n")
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('utf-8'))
    # Fecha conex�o com o servidor
    s.close()
