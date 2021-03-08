import socket
import os
import pickle


def busca_arquivo_rec(nome, dir):
    lista_dir = []
    lista_resp = []
    lista_dir.append(dir)

    while lista_dir:
        dir_atual = lista_dir[0]
        l = []
        try:
            l = os.listdir(dir_atual)
        except:
            pass
        for i in l:
            arq = os.path.join(dir_atual, i)
            if os.path.isfile(arq) and i == nome:
                lista_resp.append(arq)
            elif os.path.isdir(arq):
                lista_dir.append(arq)
        lista_dir.remove(dir_atual)
    return (lista_resp)

# Definir função busca_arquivo_rec aqui

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()

print("Servidor de nome", host, "esperando conexão na porta", porta)
while True:
    # Aceita alguma conexão
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(1024)
    nome = msg.decode('utf-8')
    # Procura no diretório do usuário apenas
    dir = os.environ['HOMEPATH']
    # Faz a busca do nome
    lista = busca_arquivo_rec(nome, dir)
    # Gera a lista a ser enviada:
    # esta lista contém o caminho completo e o tamanho em bytes
    lista_send = []
    for path in lista:
        tamanho = os.stat(path).st_size
        lista_send.append((path, tamanho))

    # Converte de lista para bytes
    bytes = pickle.dumps(lista_send)
    # Envia os bytes
    socket_cliente.send(bytes)
    # Fecha a conexão com o cliente
    socket_cliente.close()

# Fecha conexão do servidor
socket_servidor.close()