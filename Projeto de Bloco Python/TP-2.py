import pygame, sys, platform, psutil
import pygame.display

class Contexto():
    terminou = False
    tela = None
    largura_tela = 800
    altura_tela = 600
    posicao = 0
    HTML = ''
    carregou = False
    loop = 0



def corpo(contexto):

    # VARIÁVEIS BÁSICAS PARA OBTER INFORMAÇÃO DO SISTEMA
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0)
    disco = psutil.disk_usage('.')


    #AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS
    mem = psutil.virtual_memory()
    larg = contexto.largura_tela - 2 * 20
    s1.fill(FUNDO)
    pygame.draw.rect(s1, COR1, (20, 50, larg, 70))
    contexto.tela.blit(s1, (0, 0))
    larg = larg * mem.percent / 100
    pygame.draw.rect(s1, COR2, (20, 50, larg, 70))
    contexto.tela.blit(s1, (0, 0))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB) (Utilizando: " + str(mem.percent) + " %):"
    text = fonte.render(texto_barra, 1, COR3)
    contexto.tela.blit(text, (20, 10))

    # AQUI É MONTADO A UTILIZAÇÃO DO CPU
    largura = contexto.largura_tela - 2 * 20
    s2.fill(FUNDO)
    pygame.draw.rect(s2, COR1, (20, 70, largura, 70))
    contexto.tela.blit(s2, (0, contexto.altura_tela / 4))
    largura = largura * cpu / 100
    pygame.draw.rect(s2, COR2, (20, 70, largura, 70))
    contexto.tela.blit(s2, (0, contexto.altura_tela / 4))
    texto_barra = "Uso de CPU: (" + str(cpu) + " %):"
    texto_proc = "Cpu: (" + str(platform.processor()) + "):"
    text = fonte.render(texto_barra, 1, COR3)
    text_proc = fonte.render(texto_proc, 1, COR3)
    contexto.tela.blit(text, (20, (contexto.altura_tela / 4)))
    contexto.tela.blit(text_proc, (20, (contexto.altura_tela / 4) + 30))

    # AQUI É MONTADO A UTILIZAÇÃO DO HD
    largura = contexto.largura_tela - 2 * 20
    s3.fill(FUNDO)
    pygame.draw.rect(s3, COR1, (20, 50, largura, 70))
    contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
    largura = largura * disco.percent / 100
    pygame.draw.rect(s3, COR2, (20, 50, largura, 70))
    contexto.tela.blit(s3, (0, 2 * contexto.altura_tela / 4))
    texto_barra = "Uso de Disco: (" + str(disco.percent) + " %):"
    text = fonte.render(texto_barra, 1, COR3)
    contexto.tela.blit(text, (20, (2 * contexto.altura_tela / 4)))




def montar_tela(contexto):
    corpo(contexto)


def main():
    input_text = ''
    capturou = False
    gerou_relatorio = False
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

    fonte = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 28)
    fonteMenor = pygame.font.Font('C:\\Windows\\Fonts\\Calibri.ttf', 17)
    pygame.display.set_caption("Gerenciador de tarefas.")

    clicked = False
    BRANCO = (255, 255, 255)
    FUNDO = (0, 0, 0)
    TEXTO = (255, 255, 255)
    COR1 = (255, 0, 0)
    COR2 = (0, 12, 255)
    COR3 = (46, 255, 0)
    COR4 = (244, 67, 54)

    #AQUI É MONTADO A UTILIZAÇÃO DAS MEMORIAS
    s1 = pygame.surface.Surface((800, 600 / 4))
    s2 = pygame.surface.Surface((800, 600 / 4))
    s3 = pygame.surface.Surface((800, 600 / 4))
    s4 = pygame.surface.Surface((800, 600 / 4))

    main()
