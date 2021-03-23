import socket, time, pickle

# Função que imprime a lista formatada
def imprime(l):
    print(f"""
        pid: {l['pid']}
        ip: {l['ip']}
        mem_total: {l['memoria_total']}
        mem_usado: {l['memoria_usada']}
        cpu: {l['cpu']}
        disco_total: {l['disco_total']}
        disco_usado: {l['disco_usado']}
        
    """)

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9999))
    msg = ' '
    for i in range(10):
        # Envia mensagem vazia apenas para indicar a requisição
        s.send(msg.encode('ascii'))
        bytes = s.recv(1024)
        # Converte os bytes para lista
        dicionario = pickle.loads(bytes)
        imprime(dicionario)
        time.sleep(2)
    msg = 'fim'
    s.send(msg.encode('ascii'))
except Exception as erro:
    print(str(erro))

# Fecha o socket
s.close()

input("Pressione qualquer tecla para sair...")