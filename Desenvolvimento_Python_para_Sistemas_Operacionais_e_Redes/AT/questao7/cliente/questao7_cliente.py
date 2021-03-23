import os
import pickle
import socket, time

def motrar_dados(dado):
    print(f""" 
    memoria total: {dado['mem_total']},
    memoria disponível: {dado['mem_disp']}
    """)

host = socket.gethostname()
porta = 9999

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (host, porta)
msg = ' '
envia = msg.encode('UTF-8')

for i in range(4):
    if i == 3:
        msg = 'memoria'
        envia = msg.encode('UTF-8')
    udp.sendto(envia, dest)
    udp.settimeout(5.0)
    try:
        (msg_serv, dest) = udp.recvfrom(1024)
        resposta = pickle.loads(msg_serv)
        if resposta != '':
            motrar_dados(resposta)
            break
        else:
            print('processando')
    except Exception as erro:
        print(str(erro))
        input("Pressione qualquer tecla para sair...")
        continue

udp.close()

