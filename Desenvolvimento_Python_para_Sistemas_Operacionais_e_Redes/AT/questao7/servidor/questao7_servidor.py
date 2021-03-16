import socket, os

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))
socket_servidor.listen()


(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

# Recebe pedido do cliente:
msg_bytes = "informe o nome do arquivo".encode('utf-8')
socket_cliente.send(msg_bytes)
nome_arquivo = socket_cliente.recv(50).decode('utf-8')


pathLocal = os.environ["IDE_PROJECT_ROOTS"]
caminho = f'{pathLocal}/AT/questao6/servidor/{nome_arquivo}'
print(caminho)
if os.path.exists(caminho):


    arquivo_p = open(caminho, 'rb')
    arquivo = arquivo_p.read()

    socket_cliente.send(f'{len(arquivo)}'.encode('utf-8'))
    socket_cliente.send(arquivo)
    arquivo_p.close()

else:
    socket_cliente.send(b'-1')