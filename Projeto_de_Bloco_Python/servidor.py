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
    msg = socket_cliente.recv(10)
    response = msg.decode('ascii')

    # Gera a lista de resposta
    info_cpu = cpuinfo.get_cpu_info()
    a = info_cpu['brand_raw']
    pid = os.getpid()
    disco = psutil.disk_usage('.')
    memoria = psutil.virtual_memory()
    perc_mem = psutil.cpu_percent()
    p = psutil.Process(pid)

    if response == 'init':
        resposta = {
            'pid': os.getpid(),
            'ip': socket.gethostbyname(socket.gethostname()),
            'processador_nome': info_cpu['brand_raw'],
            'arquitetura': info_cpu['arch'],
            'palavra': info_cpu['bits'],
            'frequencia': info_cpu['hz_actual_friendly'],
            'nucleos': info_cpu['count'],
            'cpu_nome': p.name(),
            'temp_usuario': p.cpu_times().user,
            'executavel': p.exe(),
            'temp_criacao': p.create_time(),
            'nr_threads': p.num_threads(),
            'perc_mem': psutil.cpu_percent(),
            'memoria_total': memoria.total,
            'memoria_usada': memoria.available,
            'memoria_percent': memoria.percent,
            'cpu': psutil.cpu_percent(interval=0),
            'disco_total': disco.total,
            'disco_usado': disco.used,
            'disco_percent': disco.percent

        }

    elif response == 'get':
        resposta = {
            'ip': socket.gethostbyname(socket.gethostname())
        }
        bytes_resp = pickle.dumps(resposta)
        socket_cliente.send(bytes_resp)

    elif response == 'fim':
        break

    bytes_resp = pickle.dumps(resposta)
    socket_cliente.send(bytes_resp)

socket_cliente.close()

