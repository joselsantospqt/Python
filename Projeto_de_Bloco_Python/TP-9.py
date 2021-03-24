import pygame
import platform
import psutil
import cpuinfo
import os
import time
import sched
import subprocess
import nmap
import socket, sys, pickle
import asyncio
import aiohttp
import concurrent.futures


class Contexto:
    terminou = False
    tela = None
    largura_tela = 1024
    altura_tela = 900
    loop = 0
    count = 0
    pagina = 0
    scroll_y = 0
    conexao = None

def update_conexao(contexto):
    atualiza = atualiza_servidor()
    contexto.conexao['memoria_usada'] = atualiza['memoria_usada']
    contexto.conexao['memoria_percent'] = atualiza['memoria_percent']
    contexto.conexao['perc_mem'] = atualiza['perc_mem']

def atualiza_servidor():
    try:
        m = 'requestUpdate'
        update.send(m.encode('UTF-8'))

        bytes = update.recv(50000)
        atualizou = pickle.loads(bytes)

        return atualizou

    except Exception as erro:
        print(str(erro))


def conexao(m):
    try:
        # Tenta se conectar ao servidor
        update.connect((socket.gethostname(), 9999))

        mensagem = m
        update.send(mensagem.encode('UTF-8'))

        bytes = update.recv(50000)
        retorno = pickle.loads(bytes)

        #mensagem = 'fim'
        #update.send(mensagem.encode('UTF-8'))

        return retorno



    except Exception as erro:
        print(str(erro))

    # Fecha o socket
    #tcp.close()

    input("Pressione qualquer tecla para sair...")


def retorna_dados_rede(ip):
    return_codes = dict()
    host_validos = []

    ip_lista = ip.split('.')
    base_ip = ".".join(ip_lista[0:3]) + '.'

    return_codes[base_ip + '{0}'.format(1)] = retorna_codigo_ping(base_ip + '{0}'.format(1))

    if return_codes[base_ip + '{0}'.format(1)] == 0:
        host_validos.append(base_ip + '{0}'.format(1))

    return host_validos


def funcao_complementar_rede(host_validos):
    vScannner = nmap.PortScanner()
    for i in host_validos:
        try:
            print("\nCarregando Scan ...")
            vScannner.scan(i)
            print("\nCompleto!")
            ipv4 = vScannner[i]['addresses']['ipv4']
            mac = vScannner[i]['addresses']['mac']
        except:
            pass

    return ipv4, mac


def retorna_codigo_ping(hostname):
    """Usa o utilitario ping do sistema operacional para encontrar   o host. ('-c 5') indica, em sistemas linux, que deve mandar 5   pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3   milisegundos por uma resposta. Esta funcao retorna o codigo de   resposta do ping """

    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args,
                              stdout=open(os.devnull, 'w'),
                              stderr=open(os.devnull, 'w'))
    return ret_cod


def corpo(contexto):
    # AQUI É MONTADO O FUNDO DOS DADOS DO CPU
    s1.fill(BRANCO)
    contexto.tela.blit(s1, (0, contexto.scroll_y))

    # AQUI É MONTADO A PÁGINAÇÃO
    if contexto.pagina == 0:
        s = "CPU: " + str(contexto.conexao['processador_nome'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 0))

        s = "Arquitetura: " + str(contexto.conexao['arquitetura'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 20))

        s = "Palavra: " + str(contexto.conexao['palavra'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 40))

        s = "Frequência: " + str(contexto.conexao['frequencia'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 60))

        s = "Núcleos: " + str(contexto.conexao['nucleos'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 80))

        # AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS
        largura = contexto.largura_tela - 2 * 20
        s2.fill(FUNDO)
        pygame.draw.rect(s2, COR1, (20, 110, largura, 70))
        contexto.tela.blit(s2, (0, 300))
        largura = largura * contexto.conexao['memoria_percent'] / 100
        pygame.draw.rect(s2, COR2, (20, 110, largura, 70))
        contexto.tela.blit(s2, (0, 300))
        total = round(contexto.conexao['memoria_total'] / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Memória (Total: " + str(total) + "GB) (Utilizando: " + str(
            contexto.conexao['memoria_percent']) + " %):"
        text = fonte.render(texto_barra, 1, COR3)
        contexto.tela.blit(text, (20, 350))

        # AQUI É MONTADO A UTILIZAÇÃO DO HD
        largura = contexto.largura_tela - 2 * 20
        s3.fill(FUNDO)
        pygame.draw.rect(s3, COR1, (20, 110, largura, 70))
        contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
        largura = largura * contexto.conexao['disco_percent'] / 100
        pygame.draw.rect(s3, COR2, (20, 110, largura, 70))
        contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
        texto_barra = "Uso de Disco: (" + str(contexto.conexao['disco_percent']) + " %):"
        text = fonte.render(texto_barra, 1, COR3)
        contexto.tela.blit(text, (20, 500))

    elif contexto.pagina == 1:

        def carrega_memoria():
            s = "Memória: " + str(contexto.conexao['memoria_percent']) + "%"
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 0 ))
            print('ESCALONADAS DA FUNÇÃO - carrega_memoria:', time.ctime())

        def carrega_HD():
            s = "HD: " + str(contexto.conexao['disco_percent']) + "%"
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 20))
            print('ESCALONADAS DA FUNÇÃO - carrega_HD:', time.ctime())

        def carrega_rede():
            s = "IP: " + str(contexto.conexao['ip'])
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 40))
            print('ESCALONADAS DA FUNÇÃO - carrega_rede:', time.ctime())

        def carrega_dados_cpu():

            print('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.process_time()))

            s = "Nome: " + str(contexto.conexao['cpu_nome'])
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 60))

            s = "Tempo de usuário: " + str(contexto.conexao['temp_usuario'])
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 80))

            s = "Executável: " + str(contexto.conexao['executavel'])
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (20, 100))

            s = "Tempo de criação: " + str(time.ctime(contexto.conexao['temp_criacao']))
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (350, 0))

            s = "Número de threads: " + str(contexto.conexao['nr_threads'])
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (350, 20))

            perc_mem = '{:6.2f}'.format(contexto.conexao['perc_mem'])
            s = "Percentual de uso de CPU: " + str(perc_mem) + "%"
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (350, 40))

            mem = '{:6.2f}'.format(contexto.conexao['memoria_percent'])
            s = "Uso de memória: " + str(mem) + "MB"
            text = fonteMenor.render(s, 1, FUNDO)
            contexto.tela.blit(text, (350, 60))
            time.sleep(2)

            print('ESCALONADAS DA FUNÇÃO - carrega_dados_cpu:', time.ctime())

        def carrega_info_rede():

            dados_info_rede = contexto.conexao['info-rede']
            dados_processo = contexto.conexao['dados_processos']
            interfaces = psutil.net_if_addrs()

            ipv4 = ''
            netmask = ''
            mac = ''

            margin = 160
            titulo = " Informações de redes: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, margin + contexto.scroll_y))

            # AQUI FORMATO E PREENCHO VÁRIAVEIS ANTES DE EXIBIR NA TELA

            for i in dados_info_rede:
                io_status = psutil.net_io_counters(pernic=True)
                margin += 30
                nome = fonteMenor.render(i + " :", 1, BRANCO)
                contexto.tela.blit(nome, (10, margin))

                if i == 'Ethernet':
                    margin += 25

                    titulo = "IP: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (10, margin))

                    titulo = "Gateway: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (130, margin))

                    titulo = "Máscara: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (300, margin))

                    titulo = "Dados Enviados: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (430, margin))

                    titulo = "Dados Recebidos: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (580, margin))

                    titulo = "Pacotes Enviados: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (725, margin))

                    titulo = "Pacotes Recebidos: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (880, margin))

                    for j in interfaces[i]:

                        if str(j.family) == 'AddressFamily.AF_INET':
                            ipv4 = j.address
                            netmask = j.netmask
                        if str(j.family) == 'AddressFamily.AF_LINK':
                            mac = j.address

                    ip01 = fonteMenor.render(str(ipv4), 1, BRANCO)
                    gateway = fonteMenor.render(str(mac), 1, BRANCO)
                    mascara = fonteMenor.render(str(netmask), 1, BRANCO)
                    db_enviado = fonteMenor.render(str(io_status[i].bytes_sent) + ' bytes', 1, BRANCO)
                    db_recebido = fonteMenor.render(str(io_status[i].bytes_recv) + ' bytes', 1, BRANCO)
                    pc_enviado = fonteMenor.render(str(io_status[i].packets_sent) + ' bytes', 1, BRANCO)
                    pc_recebido = fonteMenor.render(str(io_status[i].packets_recv) + ' bytes', 1, BRANCO)

                    margin += 25
                    contexto.tela.blit(ip01, (10, margin))
                    contexto.tela.blit(gateway, (130, margin))
                    contexto.tela.blit(mascara, (300, margin))
                    contexto.tela.blit(db_enviado, (430, margin))
                    contexto.tela.blit(db_recebido, (580, margin))
                    contexto.tela.blit(pc_enviado, (725, margin))
                    contexto.tela.blit(pc_recebido, (880, margin))

                    margin += 25

                else:

                    margin += 25

                    titulo = "IP: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (10, margin))

                    titulo = "Gateway: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (130, margin))

                    titulo = "Máscara: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (300, margin))

                    titulo = "Dados Enviados: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (430, margin))

                    titulo = "Dados Recebidos: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (580, margin))

                    titulo = "Pacotes Enviados: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (725, margin))

                    titulo = "Pacotes Recebidos: "
                    text = fonteMenor.render(titulo, 1, BRANCO)
                    contexto.tela.blit(text, (880, margin))

                    for j in interfaces[i]:
                        if str(j.family) == 'AddressFamily.AF_INET':
                            ipv4 = j.address
                            netmask = j.netmask
                        if str(j.family) == 'AddressFamily.AF_LINK':
                            mac = j.address

                    ip01 = fonteMenor.render(ipv4, 1, BRANCO)
                    gateway = fonteMenor.render(mac, 1, BRANCO)
                    mascara = fonteMenor.render(netmask, 1, BRANCO)
                    DadosRede = fonteMenor.render(str(io_status[i]), 1, BRANCO)
                    db_enviado = fonteMenor.render(str(io_status[i].bytes_sent) + ' bytes', 1, BRANCO)
                    db_recebido = fonteMenor.render(str(io_status[i].bytes_recv) + ' bytes', 1, BRANCO)
                    pc_enviado = fonteMenor.render(str(io_status[i].packets_sent) + ' bytes', 1, BRANCO)
                    pc_recebido = fonteMenor.render(str(io_status[i].packets_recv) + ' bytes', 1, BRANCO)

                    margin += 25
                    contexto.tela.blit(ip01, (10, margin))
                    contexto.tela.blit(gateway, (130, margin))
                    contexto.tela.blit(mascara, (300, margin))
                    contexto.tela.blit(db_enviado, (430, margin))
                    contexto.tela.blit(db_recebido, (580, margin))
                    contexto.tela.blit(pc_enviado, (725, margin))
                    contexto.tela.blit(pc_recebido, (880, margin))

                    margin += 25

            margin = 500
            titulo = " Informações de dados de Processo: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, margin + contexto.scroll_y))

            margin += 25

            titulo = "PID: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (10, margin + contexto.scroll_y))

            titulo = "Laddr - Address: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (100, margin + contexto.scroll_y))

            titulo = "Raddr - Address: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (350, margin + contexto.scroll_y))

            titulo = "Status: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (650, margin + contexto.scroll_y))

            for i in dados_processo:
                pid = fonteMenor.render(str(i.pid), 1, BRANCO)
                laddr = fonteMenor.render(str(i.laddr), 1, BRANCO)
                raddr = fonteMenor.render(str(i.raddr), 1, BRANCO)
                status = fonteMenor.render(str(i.status), 1, BRANCO)

                margin += 25
                contexto.tela.blit(pid, (10, margin + contexto.scroll_y))
                contexto.tela.blit(laddr, (100, margin + contexto.scroll_y))
                contexto.tela.blit(raddr, (350, margin + contexto.scroll_y))
                contexto.tela.blit(status, (650, margin + contexto.scroll_y))

        with concurrent.futures.ThreadPoolExecutor() as item:
            for i in range(5):
                if i == 0:
                    item.submit(carrega_memoria)
                elif i == 1:
                    item.submit(carrega_HD)
                elif i == 2:
                    item.submit(carrega_rede)
                elif i == 3:
                    item.submit(carrega_info_rede)
                elif i == 4:
                    item.submit(carrega_dados_cpu)

    elif contexto.pagina == 2:

        s = "Sistema: " + str(platform.system())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 0))

        s = "Nome do PC: " + str(platform.node())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 20))

        s = "Versão do Windows: " + str(platform.version())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 40))

        s = "Maquina: " + str(platform.machine())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 60))

        s = "IP: " + contexto.conexao['ipv4']
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (350, 0))

        s = "MAC: " + contexto.conexao['mac']
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (350, 20))


        # AQUI É MONTADO A EXIBIÇÃO DO DIRETORIO
        if len(contexto.conexao['lista_arq']) > 0:
            titulo = "Arquivos: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, 160))

            margin = 160
            for i in contexto.conexao['lista_arq']:
                margin += 20
                nome_arquivo = i
                text = fonteMenor.render(nome_arquivo, 1, BRANCO)
                contexto.tela.blit(text, (5, margin))

            # AQUI EU CRIO AS COLUNAS
            margin += 50
            titulo = "Nome do Arquivo: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, margin))

            titulo = "Tamanho: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (150, margin))

            titulo = "Tempo de criação: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (250, margin))

            titulo = "Tempo de modificação: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (490, margin))

            dic = {}
            for i in contexto.conexao['lista_arq']:
                    index = contexto.conexao['lista_arq'].index(i)
                    dic[i] = []
                    for j in contexto.conexao['dic'][index]:
                        dic[i].append(j)


            # AQUI FORMATO E PREENCHO VÁRIAVEIS ANTES DE EXIBIR NA TELA
            for i in dic:
                margin += 20
                nome = fonteMenor.render(i, 1, BRANCO)
                kb = (dic[i][0] / 1000)
                formataTamanho = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
                tamanho = fonteMenor.render(formataTamanho, 1, BRANCO)
                criacao = fonteMenor.render(str(time.ctime(dic[i][1])), 1, BRANCO)
                modificacao = fonteMenor.render(str(time.ctime(dic[i][2])), 1, BRANCO)

                contexto.tela.blit(nome, (5, margin))
                contexto.tela.blit(tamanho, (150, margin))
                contexto.tela.blit(criacao, (250, margin))
                contexto.tela.blit(modificacao, (490, margin))

        if len(contexto.conexao['lista_dir']) > 0:
            titulo = "Diretórios: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (150, 160))

            margin = 160
            for i in contexto.conexao['lista_dir']:
                margin += 20
                nome_pasta = i
                text = fonteMenor.render(nome_pasta, 1, BRANCO)
                contexto.tela.blit(text, (150, margin))

    # AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS


def montar_tela(contexto):
    corpo(contexto)


def main():
    contexto = Contexto()
    tela = pygame.display.set_mode((contexto.largura_tela, contexto.altura_tela))
    clock = pygame.time.Clock()
    contexto.tela = tela

    print("\nIniciando Conexão com o banco ...")
    retorno = conexao('init')
    if retorno != '':
        contexto.conexao = retorno
    print("Concluido ! ")

    print("\nIniciando Informações Redes Local ...")

    with concurrent.futures.ThreadPoolExecutor() as item:
        lista = []
        lista.append(item.submit(retorna_dados_rede, contexto.conexao['ip']))

    ipv4, mac = funcao_complementar_rede(lista[0].result())
    contexto.conexao['ipv4'] = ipv4
    contexto.conexao['mac'] = mac

    print("Concluido ! ")

    while not contexto.terminou:

        # Atualiza o desenho na tela
        pygame.display.update()
        tela.fill(FUNDO)

        montar_tela(contexto)
        update_conexao(contexto)

        # Checar os eventos do usuario:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                press = pygame.key.get_pressed()

                if press[pygame.K_ESCAPE]:
                    contexto.terminou = True

                if press[pygame.K_LEFT]:
                    if contexto.pagina > 0:
                        contexto.pagina -= 1

                if press[pygame.K_RIGHT]:
                    if contexto.pagina <= 1:
                        contexto.pagina += 1

            if event.type == pygame.QUIT:
                contexto.terminou = True

                update.close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: contexto.scroll_y = min(contexto.scroll_y + 15, 0)
                if event.button == 5: contexto.scroll_y = max(contexto.scroll_y - 15, -300)

        pygame.display.flip()
        clock.tick(30)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':
    print("\nIniciando Pygame ...")
    pygame.init()

    fonte = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fonteMenor = pygame.font.Font('C:\\Windows\\Fonts\\Calibri.ttf', 17)
    pygame.display.set_caption("Gerenciador de tarefas TP-4.")
    update = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    BRANCO = (255, 255, 255)
    FUNDO = (0, 0, 0)
    TEXTO = (255, 255, 255)
    COR1 = (255, 0, 0)
    COR2 = (0, 12, 255)
    COR3 = (46, 255, 0)
    COR4 = (244, 67, 54)

    s1 = pygame.surface.Surface((1024, 600 / 4))
    s2 = pygame.surface.Surface((1024, 600 / 4))
    s3 = pygame.surface.Surface((1024, 600 / 4))
    s4 = pygame.surface.Surface((1024, 600 / 4))

    main()
