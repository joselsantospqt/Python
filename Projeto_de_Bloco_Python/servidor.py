import socket, psutil, pickle
import cpuinfo

# Cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
tcp.bind((host, porta))
tcp.listen()

print("Servidor de nome", host, "esperando conexão na porta", porta)
# trocar de lista para dict

import os

user = os.getlogin()

(socket_cliente, addr) = tcp.accept()
print("Conectado a:", str(addr))

response = []
while True:
    # Recebe pedido do cliente:
    response.clear()
    mensagem = socket_cliente.recv(4096)
    reposta = mensagem.decode('UTF-8')

    # Gera a lista de resposta
    info_cpu = cpuinfo.get_cpu_info()
    pid = os.getpid()
    disco = psutil.disk_usage('.')
    memoria = psutil.virtual_memory()
    perc_mem = psutil.cpu_percent(interval=None)
    p = psutil.Process(pid)

    if reposta == 'init':
        response = {
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

    elif reposta == 'get':
        response = {
            'ip': socket.gethostbyname(socket.gethostname())
        }

    elif reposta == 'fim':
        break

    bytes = pickle.dumps(response)
    socket_cliente.send(bytes)

socket_cliente.close()

input("Pressione qualquer tecla para sair...")  # Espera usu�rio ler

