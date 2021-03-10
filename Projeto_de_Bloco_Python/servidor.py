import socket, psutil, pickle
import cpuinfo

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
socket_servidor.bind((host, porta))
socket_servidor.listen()

print("Servidor de nome", host, "esperando conexão na porta", porta)

# login
# psutil.cpu_count()
# qtd de psutil.pids()
# psutil.cpu_percent()
# mem = psutil.virtual_memory()
# mem_percent = mem.used / mem.total

# trocar de lista para dict

import os
user = os.getlogin()


(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    # Recebe pedido do cliente:
    msg = socket_cliente.recv(4)
    if msg.decode('ascii') == 'fim':
        break
    # Gera a lista de resposta

    mem = psutil.virtual_memory()
    pid = os.getpid()
    resposta = {
        ## 'info_cpu': cpuinfo.get_cpu_info(),
        'pid': os.getpid(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'memoria_total': psutil.virtual_memory().total,
        'memoria_usada': psutil.virtual_memory().available,
        'cpu': psutil.cpu_percent(interval=0),
        'disco_total': psutil.disk_usage('.').total,
        'disco_usado': psutil.disk_usage('.').used
    }

    bytes_resp = pickle.dumps(resposta)
    # Envia os dados
    socket_cliente.send(bytes_resp)

# Fecha socket do servidor e cliente
socket_cliente.close()
socket_servidor.close()


