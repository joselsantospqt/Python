import requests
import pygame
import io
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Contexto():
    terminou = False
    tela = None
    largura_tela = 800
    altura_tela = 600
    titulo = ''
    posicao = 0
    git_name = ''
    HTML = ''
    carregou = False
    return_response = False
    loop = 0
    total_repositorios = 0


class Pessoa():
    nome = ''
    foto = ''
    nick = ''
    notas = ''


class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.Font("C:\\Windows\\Fonts\\Arial.ttf", 10)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def carregaDados(contexto):

    if len(contexto.git_name) <= 0:
        nome = 'not_found'
    else:
        nome = contexto.git_name

    response = requests.get('https://github.com/' + nome)

    if response.status_code == 200:
        contexto.return_response = True
        dados = response.text
        pessoa = Pessoa()

        soup = BeautifulSoup(dados, 'html.parser')

        print('Carregando ->', soup.title.text)

        content_el = soup.find('main', {'id': 'js-pjax-container'})

        img_perfil_usuario = content_el.find('img', class_='avatar avatar-user width-full border bg-white')
        if img_perfil_usuario:
            pessoa.foto = img_perfil_usuario['src']

        nome_perfil_usuario = content_el.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
        if nome_perfil_usuario:
            pessoa.nome = nome_perfil_usuario.text

        nick_perfil_usuario = content_el.find('span', class_='p-nickname vcard-username d-block')
        if nick_perfil_usuario:
            pessoa.nick = nick_perfil_usuario.text

        notas_perfil_usuario = content_el.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
        if notas_perfil_usuario:
            pessoa.notas = notas_perfil_usuario.text

        usuario.append(pessoa)
        carregaRepositorio(contexto)
    else:
        contexto.return_response = False


def carregaRepositorio(contexto):

    nome = contexto.git_name
    repositorios = []

    response = requests.get('https://github.com/' + nome + '?tab=repositories')

    if response.status_code == 200:
        dados = response.text

        soup = BeautifulSoup(dados, 'html.parser')
        print('Carregando ->', soup.title.text)

        content_el = soup.find('div', {'id': 'user-repositories-list'})

        total_itens = content_el.find_all('li')
        contexto.total_repositorios = len(total_itens)

        for itens in total_itens:
            sets_ = {}
            titulo_repositorio = itens.find('h3', class_='wb-break-all')
            "print(titulo_repositorio)"
            sets_['titulo'] = titulo_repositorio.text.strip().replace('\n', '')

            descriacao_repositorio = itens.find('p', class_='col-9 d-inline-block text-gray mb-2 pr-4')
            "print(descriacao_repositorio)"
            if descriacao_repositorio:
                sets_['subtitulo'] = descriacao_repositorio.text.strip().replace('\n', '')
            else:
                sets_['subtitulo'] = 'Não existe Descrição'

            # Sei que existe forma melhor de se fazer isso
            try:
                star_repositorio = itens.find('a', class_='muted-link mr-3')
                if star_repositorio is not None:
                    sets_['star'] = int(star_repositorio.text.strip().replace('\n', ''))
                else:
                    sets_['star'] = 0
            except:
                a = star_repositorio
                a = str(a)
                b = re.sub('[^0-9]', '', a)
                sets_['star'] = b[-4::]

            repositorios.append(sets_)
        usuario.append(repositorios)
    else:
        contexto.total_repositorios = 1
        sets_ = {}
        sets_['titulo'] = 'Não existe Descrição'
        sets_['subtitulo'] = 'Não existe Descrição'
        sets_['star'] = 0
        repositorios.append(sets_)
        usuario.append(repositorios)


def gerarRelatorio(usuario):
    import csv
    relatorio = []
    sets_ = {}

    sets_['titulo'] = "Olá " + usuario[0].nome + " Aqui está seu relatório"
    sets_['nome'] = usuario[0].nome
    sets_['nick'] = usuario[0].nick
    sets_['notas'] = usuario[0].notas
    sets_['repositorio'] = len(usuario[1])

    relatorio.append(sets_)

    titulos = relatorio[0].keys()

    with open('relatorio.csv', 'w', encoding='cp1252') as output_file:
        dict_writer = csv.DictWriter(output_file, titulos)
        dict_writer.writeheader()
        dict_writer.writerows(relatorio)


def montar_tela(contexto):
    cabecalho(contexto)
    corpo(contexto)


def cabecalho(contexto):
    tela = contexto.tela
    texto_surface = fonte.render('BEM VINDO AO SISTEMA', True, TEXTO)
    tela.blit(texto_surface, dest=(0, 0))
    pygame.draw.line(tela, TEXTO, (0, 40), (contexto.largura_tela, 40))


def corpo(contexto):

    input_rect = pygame.Rect(20, 90, 180, 40)
    color = pygame.Color('lightskyblue3')
    tela = contexto.tela

    botao_pesquisar.draw(tela, (0, 0, 0))
    pygame.draw.rect(tela, color, input_rect, 2)

    texto_surface = fonte.render(contexto.git_name, True, TEXTO)
    tela.blit(texto_surface, (input_rect.x + 0, input_rect.y + 0))

    input_rect.w = max(100, texto_surface.get_width() + 10)

    texto_surface = fonte.render('Escreva seu nick do github', True, TEXTO)
    tela.blit(texto_surface, dest=(20, 50))


def montaDados(contexto):
    tela = contexto.tela
    if contexto.loop == 0:
        carregaDados(contexto)
        contexto.loop += 1

    if contexto.return_response:
        if contexto.carregou is False:
            contexto.carregou = True

        texto_surface = fonte.render(usuario[0].nome, True, COR1)
        tela.blit(texto_surface, dest=(300, 150))

        texto_surface = fonte.render(usuario[0].nick, True, COR2)
        tela.blit(texto_surface, dest=(300, 190))

        texto_surface = fonteMenor.render(usuario[0].notas, True, COR3)
        tela.blit(texto_surface, dest=(300, 230))

        if len(usuario[1]) > 0:
            texto_surface = fonteMenor.render('Repositorio: ' + str(usuario[1][contexto.posicao]['titulo']), True, COR4)
            tela.blit(texto_surface, dest=(300, 270))

            texto_surface = fonteMenor.render('Descrição:' + str(usuario[1][contexto.posicao]['subtitulo']), True, COR4)
            tela.blit(texto_surface, dest=(300, 290))

            texto_surface = fonteMenor.render('Stars: ' + str(usuario[1][contexto.posicao]['star']), True, COR4)
            tela.blit(texto_surface, dest=(300, 310))

        else:
            texto_surface = fonteMenor.render('ESSE USUARIO NÃO CONTEM REPOSITÓRIO', True, COR4)
            tela.blit(texto_surface, dest=(300, 270))

        image_str = urlopen(usuario[0].foto).read()
        image_file = io.BytesIO(image_str)
        img = pygame.image.load(image_file)
        img = pygame.transform.scale(img, (200, 200))
        tela.blit(img, dest=(50, 150))

        botao_relatorio.draw(tela, (0, 0, 0))

    else:
        texto_surface = fonte.render('DEU ERRO MEU IRMÃO, TENTE DNV', True, COR1)
        tela.blit(texto_surface, dest=(50, 150))

    '''texto_surface = fonte.render('CARREGANDO DADOS ...', True, COR1)
    tela.blit(texto_surface, dest=(300, 150))'''


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

                # magica
                contexto.titulo = ''

                if press[pygame.K_LEFT]:
                    if contexto.posicao == 0:
                        contexto.posicao = 0
                    else:
                        contexto.posicao -= 1

                if press[pygame.K_RIGHT]:
                    total = contexto.total_repositorios - 1
                    if contexto.posicao < total:
                        contexto.posicao += 1

                if press[pygame.K_ESCAPE]:
                    contexto.terminou = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_pesquisar.isOver(pos):
                    capturou = True

                if botao_relatorio.isOver(pos):
                    gerou_relatorio = True

            if event.type == pygame.MOUSEMOTION:
                if botao_pesquisar.isOver(pos):
                    botao_pesquisar.color = COR1
                    botao_pesquisar.text = 'CARREGANDO'
                else:
                    botao_pesquisar.color = BRANCO
                    botao_pesquisar.text = 'BUSCAR PERFIL'

                if botao_relatorio.isOver(pos):
                    botao_relatorio.color = COR1
                else:
                    botao_relatorio.color = BRANCO

            if event.type == pygame.QUIT:
                contexto.terminou = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[0:-1]
                input_text += event.unicode
                contexto.git_name = input_text

        if capturou:
            montaDados(contexto)

        if gerou_relatorio:
            gerarRelatorio(usuario)
            gerou_relatorio = False

        pygame.display.flip()
        clock.tick(60)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':
    usuario = []
    pygame.init()

    img = pygame.image.load('imagens/icon.png')
    fonte = pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf', 32)
    fonteMenor = pygame.font.Font('C:\\Windows\\Fonts\\Calibri.ttf', 17)
    pygame.display.set_caption("AT Ezekiel GIT-HUB")
    pygame.display.set_icon(img)

    clicked = False
    BRANCO = (255, 255, 255)
    FUNDO = (0, 0, 0)
    TEXTO = (255, 255, 255)
    COR1 = (255, 0, 0)
    COR2 = (0, 12, 255)
    COR3 = (46, 255, 0)
    COR4 = (244, 67, 54)

    botao_pesquisar = Button(BRANCO, 210, 90, 180, 40, 'CLIQUE AQUI')

    botao_relatorio = Button(BRANCO, 300, 380, 180, 40, 'GERAR RELATORIO')

    main()
