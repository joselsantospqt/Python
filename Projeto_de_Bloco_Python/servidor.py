import socket, psutil, pickle
import cpuinfo
import os

# Cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
tcp.bind((host, porta))
tcp.listen()

print("Servidor de nome", host, "esperando conexão na porta", porta)
# trocar de lista para dict

(socket_cliente, addr) = tcp.accept()
print("Conectado a:", str(addr))

response = []
while True:
    # Recebe pedido do cliente:
    mensagem = socket_cliente.recv(50000)
    reposta = mensagem.decode('UTF-8')

    # Gera a lista de resposta
    info_cpu = cpuinfo.get_cpu_info()
    pid = os.getpid()
    disco = psutil.disk_usage('.')
    memoria = psutil.virtual_memory()
    perc_mem = psutil.cpu_percent(interval=1)
    p = psutil.Process(pid)
    interfaces = psutil.net_if_addrs()

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
            'cpu': psutil.cpu_percent(interval=1),
            'disco_total': disco.total,
            'disco_usado': disco.used,
            'disco_percent': disco.percent,
            'info-rede': [],
            'dados_processos': [],
            'lista_arq': [],
            'lista_dir': [],
            'dic': [],

        }

        # Obtém os nomes das interfaces primeiro
        for i in interfaces:
            response['info-rede'].append(str(i))

        # Obtém os dados de processo do computador
        for i in psutil.net_connections():
            response['dados_processos'].append(i)

        # AQUI CARREGO OS ARQUIVOS DO DIRETORIO
        lista = os.listdir()
        for i in lista:
            dic = []
            if os.path.isfile(i):
                response['lista_arq'].append(i)
                dic.extend([os.stat(i).st_size, os.stat(i).st_atime, os.stat(i).st_mtime])
                response['dic'].append(dic)
            else:
                response['lista_dir'].append(i)

    elif reposta == 'requestUpdate':
        response = {
            'memoria_usada': memoria.available,
            'memoria_percent': memoria.percent,
            'perc_mem': psutil.cpu_percent(),
            'dados_processos': [],
        }
        # Obtém os dados de processo do computador
        for i in psutil.net_connections():
            response['dados_processos'].append(i)


    elif reposta == 'fim':
        break

    bytes = pickle.dumps(response)
    socket_cliente.send(bytes)

socket_cliente.close()

input("Pressione qualquer tecla para sair...")  # Espera usu�rio ler
