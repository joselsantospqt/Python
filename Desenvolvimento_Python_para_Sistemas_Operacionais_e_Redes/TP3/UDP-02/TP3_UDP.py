import os
import psutil
import socket


def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func

@rodar
def main():
    HOST = ''
    PORT = 9991
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    print(HOST)
    udp.bind(orig)
    print('Esperando receber na porta', PORT, '...')
    while True:
        (msg, cliente) = udp.recvfrom(1024)
        if '$' == msg.decode('utf-8'):
            print("Fechando conexao com", str(cliente), "...")
            cliente.close()
            break
        elif 'info' in msg.decode('utf-8'):
            msg = '\n total de armazenamento: ' + str(psutil.disk_usage(path="C:").total) + 'gb\n' + 'armazenamento disponível: ' + str(psutil.disk_usage(path="C:").free) + 'gb\n' + 'Diretório: ' + str(os.getcwd())
        else:
            msg = "Ok... " + msg.decode('utf-8')

        udp.sendto(msg.encode('utf-8'), cliente)
    input('Pressione qualquer tecla para sair...')
    udp.close()