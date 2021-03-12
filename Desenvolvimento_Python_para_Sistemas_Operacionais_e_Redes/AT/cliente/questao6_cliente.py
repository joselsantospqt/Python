import socket, time

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 8881))

    msg = s.recv(30).decode('utf-8')

    nome_arquivo = input(msg)
    nome_arquivo_bytes = nome_arquivo.encode('utf-8')
    s.send(nome_arquivo_bytes)

    tamanho = int(s.recv(10).decode('utf-8'))
    if tamanho >= 0:
        recebido = s.recv(tamanho)
        caminho = f'cliente/{nome_arquivo}'
        local = open(caminho, 'wb')
        local.write(recebido)
        local.close()
    else:
        print('não existe arquivo no servidor')

except Exception as erro:
    print(str(erro))

# Fecha o socket
s.close()

input("Pressione qualquer tecla para sair...")