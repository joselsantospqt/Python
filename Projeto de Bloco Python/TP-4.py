import pygame
import platform
import psutil
import cpuinfo
import os
import time
import subprocess


class Contexto:
    terminou = False
    tela = None
    largura_tela = 1024
    altura_tela = 900
    loop = 0
    count = 0
    pagina = 0


def corpo(contexto):

    # VARIÁVEIS BÁSICAS PARA OBTER INFORMAÇÃO DO SISTEMA
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0)
    disco = psutil.disk_usage('.')
    ip = psutil.net_connections()
    p = psutil.Process(pid)

    # AQUI É MONTADO OS DADOS DO CPU
    s1.fill(BRANCO)
    contexto.tela.blit(s1, (0, 0))
    if contexto.pagina == 0:
        s = "CPU: " + str(info_cpu['brand_raw'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 0))

        s = "Arquitetura: " + str(info_cpu['arch'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 20))

        s = "Palavra: " + str(info_cpu['bits'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 40))

        s = "Frequência: " + str(info_cpu['hz_actual_friendly'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 60))

        s = "Núcleos: " + str(info_cpu['count'])
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 80))

        s = "Percentual de uso de CPU:: " + str(p.cpu_percent(interval=1.0)) + "%"
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 100))

        # AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS
        largura = contexto.largura_tela - 2 * 20
        s2.fill(FUNDO)
        pygame.draw.rect(s2, COR1, (20, 110, largura, 70))
        contexto.tela.blit(s2, (0, 300))
        largura = largura * mem.percent / 100
        pygame.draw.rect(s2, COR2, (20, 110, largura, 70))
        contexto.tela.blit(s2, (0, 300))
        total = round(mem.total / (1024 * 1024 * 1024), 2)
        texto_barra = "Uso de Memória (Total: " + str(total) + "GB) (Utilizando: " + str(mem.percent) + " %):"
        text = fonte.render(texto_barra, 1, COR3)
        contexto.tela.blit(text, (20, 350))

        # AQUI É MONTADO A UTILIZAÇÃO DO HD
        largura = contexto.largura_tela - 2 * 20
        s3.fill(FUNDO)
        pygame.draw.rect(s3, COR1, (20, 110, largura, 70))
        contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
        largura = largura * disco.percent / 100
        pygame.draw.rect(s3, COR2, (20, 110, largura, 70))
        contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
        texto_barra = "Uso de Disco: (" + str(disco.percent) + " %):"
        text = fonte.render(texto_barra, 1, COR3)
        contexto.tela.blit(text, (20, 500))

    elif contexto.pagina == 1:

        s = "Memória: " + str(mem.percent) + "%"
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 0))

        s = "HD: " + str(disco.percent) + "%"
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 20))

        c = ip[0]
        b = c.laddr.ip
        s = "IP: " + str(b)
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 40))

        s = "Nome: " + str(p.name())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 60))

        s = "Executável: " + str(p.exe())
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 80))

        s = "Tempo de usuário: " + str(p.cpu_times().user)
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 100))

        s = "Tempo de criação:: " + str(time.ctime(p.create_time()))
        text = fonteMenor.render(s, 1, FUNDO)
        contexto.tela.blit(text, (20, 120))

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

        # AQUI CARREGO OS ARQUIVOS DO DIRETORIO
        lista = os.listdir()
        lista_arq = []
        lista_dir = []
        dic = {}
        for i in lista:
            if os.path.isfile(i):
                lista_arq.append(i)

                dic[i] = []
                dic[i].append(os.stat(i).st_size)
                dic[i].append(os.stat(i).st_atime)
                dic[i].append(os.stat(i).st_mtime)

            else:
                lista_dir.append(i)

        # AQUI É MONTADO A EXIBIÇÃO DO DIRETORIO
        if len(lista_arq) > 0:
            titulo = "Arquivos: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, 160))

            marge = 160
            for i in lista_arq:
                marge+= 20
                nome_arquivo = i
                text = fonteMenor.render(nome_arquivo, 1, BRANCO)
                contexto.tela.blit(text, (5, marge))

            # AQUI EU CRIO AS COLUNAS
            marge += 50
            titulo = "Nome do Arquivo: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (5, marge))

            titulo = "Tamanho: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (150, marge))

            titulo = "Tempo de criação: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (250, marge))

            titulo = "Tempo de modificação: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (490, marge))

            # AQUI FORMATO E PREENCHO VÁRIAVEIS ANTES DE EXIBIR NA TELA
            for i in dic:
                marge += 20
                nome = fonteMenor.render(i, 1, BRANCO)
                kb = (dic[i][0] / 1000)
                formataTamanho = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
                tamanho = fonteMenor.render(formataTamanho, 1, BRANCO)
                criacao = fonteMenor.render(str(time.ctime(dic[i][1])), 1, BRANCO)
                modificacao = fonteMenor.render(str(time.ctime(dic[i][2])), 1, BRANCO)

                contexto.tela.blit(nome, (5, marge))
                contexto.tela.blit(tamanho, (150, marge))
                contexto.tela.blit(criacao, (250, marge))
                contexto.tela.blit(modificacao, (490, marge))

        if len(lista_dir) > 0:
            titulo = "Diretórios: "
            text = fonteMenor.render(titulo, 1, BRANCO)
            contexto.tela.blit(text, (150, 160))

            marge = 160
            for i in lista_dir:
                marge += 20
                nome_pasta = i
                text = fonteMenor.render(nome_pasta, 1, BRANCO)
                contexto.tela.blit(text, (150, marge))


    # AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS



'''
        
        for i in lista:
            if os.path.isfile(i):
                dic[i] = []
            dic[i].append(os.stat(i).st_size)
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)
'''

def montar_tela(contexto):
    corpo(contexto)


def main():
    contexto = Contexto()
    tela = pygame.display.set_mode((contexto.largura_tela, contexto.altura_tela))
    clock = pygame.time.Clock()
    contexto.tela = tela

    while not contexto.terminou:

        # Atualiza o desenho na tela
        pygame.display.update()
        tela.fill(FUNDO)

        montar_tela(contexto)

        # Checar os eventos do mouse aqui:
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

        pygame.display.flip()
        clock.tick(60)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':

    pygame.init()
    info_cpu = cpuinfo.get_cpu_info()
    pid = os.getpid()

    fonte = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fonteMenor = pygame.font.Font('C:\\Windows\\Fonts\\Calibri.ttf', 17)
    pygame.display.set_caption("Gerenciador de tarefas TP-4.")

    BRANCO = (255, 255, 255)
    FUNDO = (0, 0, 0)
    TEXTO = (255, 255, 255)
    COR1 = (255, 0, 0)
    COR2 = (0, 12, 255)
    COR3 = (46, 255, 0)
    COR4 = (244, 67, 54)

    s1 = pygame.surface.Surface((1024, 600 / 4))
    s2 = pygame.surface.Surface((800, 600 / 4))
    s3 = pygame.surface.Surface((800, 600 / 4))
    s4 = pygame.surface.Surface((800, 600 / 4))
    sTelaLonga = pygame.surface.Surface((800, 600))

    main()
