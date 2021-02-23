import socket


def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func

@rodar
def main():
    HOST = "10.1.1.15"
    PORT = 9991
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    print(' Para armazenamento do disco , digite hd + Enter  \n Para sair, digite $ + Enter\n')
    msg = input("Entre com a mensagem:\n")
    udp.sendto(msg.encode('utf-8'), dest)
    while msg != '$':
        (msg, servidor) = udp.recvfrom(1024)
        print(servidor, msg.decode('utf-8'))
        msg = input()
        udp.sendto(msg.encode('utf-8'), dest)
    udp.close()