import pygame, platform, psutil
import cpuinfo


class Contexto():
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


    #AQUI É MONTADO OS DADOS DO CPU
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


    #AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS
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

    fonte = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fonteMenor = pygame.font.Font('C:\\Windows\\Fonts\\Calibri.ttf', 17)
    pygame.display.set_caption("Gerenciador de tarefas TP-3.")

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

    main()
