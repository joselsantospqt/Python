import requests
import pygame
import psutil
from bs4 import BeautifulSoup

usuario = []

class Contexto():
    terminou = False
    tela = None
    largura_tela = 800
    altura_tela = 600
    uso_cpu = 0
    titulo = ''
    posicao = 0

    HTML = ''

class Pessoa():
    nome = ''
    foto = ''
    nick = ''
    notas = ''
    status = []

def CarregaDados():
    nome = 'ebertti'
    pessoa = Pessoa()
    response = requests.get('https://github.com/' + nome)
    dados = response.text
    array = []

    soup = BeautifulSoup(dados, 'html.parser')
    print('bs4', soup.title.text)

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

    for itens in content_el.find_all('a', class_='link-gray no-underline no-wrap'):
        sets_ = {}
        s = itens.text.replace('\n', '')
        result = ''.join([i for i in s if not i.isdigit()])
        if len(result) <= 0:
          sets_['titulo'] = 'Star'
        else:
          sets_['titulo'] = result.strip()

        item_valor = itens.find('span', class_='text-bold text-gray-dark')
        sets_['valor'] = (int(item_valor.text))
        array.append(sets_)


    pessoa.status = array
    usuario.append(pessoa)
    CarregaRepositorio(nome)

def CarregaRepositorio(nome):

    repositorios = []

    response = requests.get('https://github.com/' + nome + '?tab=repositories')
    dados = response.text

    soup = BeautifulSoup(dados, 'html.parser')
    print('bs4', soup.title.text)

    content_el = soup.find('div', {'id': 'user-repositories-list'})

    for itens in content_el.find_all('li', class_='col-12 d-flex width-full py-4 border-bottom color-border-secondary public source'):
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

        repositorios.append(sets_)
    usuario.append(repositorios)

def GerarRelatorio(nome):
    import csv

    titulo = "Olá " + nome + " Aqui está seu relátorio"

    with open('relatorio.csv', 'w', encoding='cp1252') as output_file:
        dict_writer = csv.DictWriter(output_file, titulo)
        dict_writer.writeheader()
        dict_writer.writerows(usuario)

def montar_tela(contexto):
    cabecalho(contexto)
    corpo(contexto)
    rodape(contexto)

def cabecalho(contexto):
    tela = contexto.tela
    texto_surface = fonte.render('Texto superior', True, TEXTO)
    tela.blit(texto_surface, dest=(0, 0))
    pygame.draw.line(tela, TEXTO, (0, 40), (contexto.largura_tela, 40))

def rodape(contexto):
    tela = contexto.tela
    texto_surface = fonte.render('Texto Inferior', True, TEXTO)
    tela.blit(texto_surface, dest=(0, contexto.altura_tela - 36))
    pygame.draw.line(tela, TEXTO, (0, contexto.altura_tela - 40), (contexto.largura_tela, contexto.altura_tela - 40))

def corpo(contexto):


    tela = contexto.tela
    texto_surface = fonte.render(usuario[0].nome, True, TEXTO)
    tela.blit(texto_surface, dest=(100, 50))
    '''
    titulo_surface = fonte.render(str(contexto.titulo), True, TEXTO)
    tela.blit(titulo_surface, dest=(100, 100))'''

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
            if event.type == pygame.KEYDOWN:
                press = pygame.key.get_pressed()

                ## magica
                contexto.titulo = ''

                if press[pygame.K_0]:
                    contexto.posicao = 0
                if press[pygame.K_1]:
                    contexto.posicao = 1
                if press[pygame.K_2]:
                    contexto.posicao = 2
                if press[pygame.K_3]:
                    contexto.posicao = 3
                if press[pygame.K_4]:
                    contexto.posicao = 4
                if press[pygame.K_5]:
                    contexto.posicao = 5
                if press[pygame.K_6]:
                    contexto.posicao = 6
                if press[pygame.K_7]:
                    contexto.posicao = 7
                if press[pygame.K_8]:
                    contexto.posicao = 8
                if press[pygame.K_9]:
                    contexto.posicao = 9

            if event.type == pygame.QUIT:
                contexto.terminou = True

        clock.tick(60)

    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()


if __name__ == '__main__':

    pygame.init()
    CarregaDados()
    
    fonte = pygame.font.Font(pygame.font.get_default_font(), 36)

    FUNDO = (0, 0, 0)
    TEXTO = (255, 255, 255)

    main()
