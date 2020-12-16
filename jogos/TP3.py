import turtle
import random
import math
import pygame, sys
from pygame.locals import *


# region RODAR
def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func
# endregion


def questao1():
    lista = []
    for i in range(1, 6):
        lista.append(i)
    print(lista)

    if 3 in lista:
        lista.remove(3)
    elif 6 in lista:
        lista.remove(6)

    print(lista)
    tamanho = len(lista)

    print(tamanho)

    indice = len(lista) - 1
    lista[indice] = 6

    print(lista)


def questao2():
    vet = []
    for i in range(1, 6):
        num = int(input("diga um número?"))
        vet.append(num)

    print(vet)


def questao3():
    palavra = ['lucas', 'carlos', 'jose', 'lima', 'diego']
    print(palavra)
    print(palavra[::-1])


def questao4():
    t = int(input('Digite o tamanho da lista: '))
    print(f'O valor informado foi: {t}.')

    numeros = [i for i in range(t)]
    print('O resultado da questão 4 é:', numeros)

    qtd = 0
    for valor in numeros:
        if valor == 0:
            qtd += 1
    print(f'Quantidade de números iguais a zero: {qtd}.')


def questao5():
    lista = []

    while 1:
        nome = input('Digite o nome do aluno: ')
        if nome == 'Sair':
            break
        altura = int(input('Digite a altura do aluno: '))
        aluno = {'nome': nome, 'altura': altura}
        lista.append(aluno)

    def acima_media(lista):

        acima_media = []
        somatorio = 0

        for i in lista:
            somatorio += i['altura']

        media = (somatorio / len(lista))
        for i in lista:
            if i['altura'] > media:
                acima_media.append(i)

        return acima_media

    print('Alunos acima da média:')
    for i in acima_media(lista):
        print(i['nome'])


def questao6():
    lista = []

    while 1:
        palavra = input('Digite uma frase:  ')
        if palavra == 'Sair':
            break
        lista.append(palavra)

    print('As seguintes frases possuem a palavra "eu":')

    for i in lista:
        if ' eu ' in i.split():
            print(i)


def questao7():
    lista = []
    sai = False
    print("a - Mostrar lista")
    print("b - Incluir elemento")
    print("c - remover elemento")
    print("d - Apagar todos os elementos da lista")
    print("x - Sair do programa")

    while not sai:
        operacao = input("Digite a alternativa referente a operação desejada: ").lower()

        if operacao == "a":
            print(lista)
        elif operacao == "b":
            novo_elemento = input("Digite o novo elemento a ser adicionado: ")
            lista.append(novo_elemento)
        elif operacao == "c":
            remove_elemento = input("Digite o elemento a ser removido: ")
            if remove_elemento in lista:
                lista.remove(remove_elemento)
            else:
                print("Elemento não está na lista")
        elif operacao == "d":
            lista.clear()
            print("Operação concluída!")
        else:
            sair = True


def questao8():
    jogada = [random.randint(1, 6) for i in range(100)]
    um = jogada.count(1)
    dois = jogada.count(2)
    tres = jogada.count(3)
    quatro = jogada.count(4)
    cinco = jogada.count(5)
    seis = jogada.count(6)
    print('Lista de jogadas:', jogada)
    print('um:', um, 'dois:', dois, 'tres:', tres, 'quatro:', quatro, 'cinco:', cinco, 'seis:', seis)


def questao10():
    pygame.init()

    largura = 800
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    cor = (255, 0, 0)
    terminou = False
    x = 350
    y = 250

    while not terminou:
        pygame.display.update()
        tela.fill((0, 0, 0))

        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            x = x - 1
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            x = x + 1
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            y = y - 1
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            y = y + 1

        pygame.draw.rect(tela, cor, (x, y, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

    pygame.display.quit()
    pygame.quit()

def questao11():

    largura = 800
    altura = 600

    scaling_factor = 6

    x = 350
    y = 250

    rect_width, rect_height = 100, 100
    vel = 2
    black = (0, 0, 0)
    white = (255, 255, 255)
    vermelho = (255, 0, 0)
    pygame.init()
    win = pygame.display.set_mode((largura, altura))

    screen = pygame.Surface((largura, altura))

    terminou = False

    while not terminou:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        screen.fill(black)
        pygame.draw.rect(screen, vermelho, (x, y, rect_width, rect_height))

        win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
        pygame.display.update()


    pygame.display.quit()
    pygame.quit()


def questao12():
    pygame.init()

    largura = 800
    altura = 600

    win = pygame.display.set_mode((largura, altura))
    screen = pygame.Surface((largura, altura))
    cor = (255, 0, 0)
    terminou = False
    x = 350
    y = 250

    while not terminou:
        pygame.display.update()
        win.fill((0, 0, 0))

        pygame.draw.circle(win, (0, 0, 255), (x, y), 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

    pygame.display.quit()
    pygame.quit()


def questao13():
    pygame.init()

    largura = 800
    altura = 600

    win = pygame.display.set_mode((largura, altura))
    screen = pygame.Surface((largura, altura))
    cor = (118, 255, 0)
    terminou = False
    x = 350
    y = 250

    while not terminou:
        pygame.display.update()
        win.fill((0, 0, 0))

        pygame.draw.circle(win, (0, 0, 255), (x, y), 75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

    pygame.display.quit()
    pygame.quit()


def questao14():
    largura = 800
    altura = 600

    scaling_factor = 6

    x = 350
    y = 250

    rect_width, rect_height = 50, 50
    vel = 2
    black = (0, 0, 0)
    white = (255, 255, 255)
    vermelho = (255, 0, 0)
    pygame.init()
    win = pygame.display.set_mode((largura, altura))

    screen = pygame.Surface((largura, altura))

    terminou = False

    while not terminou:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        screen.fill(black)
        pygame.draw.rect(screen, vermelho, (x, y, rect_width, rect_height))

        win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
        pygame.display.update()

    pygame.display.quit()
    pygame.quit()

@rodar
def questao15():
    largura = 800
    altura = 600

    scaling_factor = 6

    x = 350
    y = 250

    rect_width, rect_height = 50, 50
    vel = 2
    white = (255, 255, 255)
    vermelho = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 99, 71)
    grey = (200, 200, 200)

    pygame.init()
    win = pygame.display.set_mode((largura, altura))

    screen = pygame.Surface((largura, altura))

    terminou = False

    while not terminou:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True




        class star:
            def __init__(self, vertice_list, rate): #Vertice_list is the list of vertice of the first star
                self.vertice_list = vertice_list
                self.rate = rate

            def show_rate(self, image):
                if 2 < self.rate <= 2.33:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(3), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(3), "blank"), 1)
                    pygame.draw.polygon(image, orange, self.no_star(4), 1)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 2.33 < self.rate <= 2.66:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(3), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(3), "blank"), 1)
                    pygame.draw.polygon(image, orange, self.no_star(4), 1)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 2.66 < self.rate <= 3:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.no_star(4), 1)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 3 < self.rate <= 3.33:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(4), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(4), "blank"), 1)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 3.33 < self.rate <= 3.66:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(4), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(4), "blank"), 1)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 3.66 < self.rate <= 4:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.no_star(4), 0)
                    pygame.draw.polygon(image, orange, self.no_star(5), 1)
                elif 4 < self.rate <= 4.33:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.no_star(4), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(5), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("first", self.no_star(5), "blank"), 1)
                elif 4.33 < self.rate <= 4.66:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.no_star(4), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(5), "color"), 0)
                    pygame.draw.polygon(image, orange, self.special_star("second", self.no_star(5), "blank"), 1)
                elif 4.66 < self.rate <= 5:
                    pygame.draw.polygon(image, orange, self.no_star(1), 0)
                    pygame.draw.polygon(image, orange, self.no_star(2), 0)
                    pygame.draw.polygon(image, orange, self.no_star(3), 0)
                    pygame.draw.polygon(image, orange, self.no_star(4), 0)
                    pygame.draw.polygon(image, orange, self.no_star(5), 0)


            def no_star(self, num_star):
                new_list = []
                if num_star == 1:
                    new_list = self.vertice_list
                elif num_star == 2:
                    for i in range(10):
                        x = self.vertice_list[i][0] + 40
                        new_list.append((x, self.vertice_list[i][1]))
                elif num_star == 3:
                    for i in range(10):
                        x = self.vertice_list[i][0] + 80
                        new_list.append((x, self.vertice_list[i][1]))
                elif num_star == 4:
                    for i in range(10):
                        x = self.vertice_list[i][0] + 120
                        new_list.append((x, self.vertice_list[i][1]))
                elif num_star == 5:
                    for i in range(10):
                        x = self.vertice_list[i][0] + 160
                        new_list.append((x, self.vertice_list[i][1]))
                return new_list

            def special_star(self, first_or_second, list_vertice, blank):
                if first_or_second == "first":
                    if blank == "color":
                        new_list = [list_vertice[7], list_vertice[8], list_vertice[9]]
                    elif blank == "blank":
                        new_list = [list_vertice[0], list_vertice[1], list_vertice[2], list_vertice[3], list_vertice[4], list_vertice[5], \
                        list_vertice[6], list_vertice[7], list_vertice[9]]
                elif first_or_second == "second":
                    if blank == "color":
                        new_list = [list_vertice[0], list_vertice[1], list_vertice[5], list_vertice[6], list_vertice[7], list_vertice[8], \
                        list_vertice[9]]
                    elif blank == 'blank':
                        new_list = [list_vertice[1], list_vertice[2], list_vertice[3], list_vertice[4], list_vertice[5]]
                return new_list

        intial_list = [(13, 0),(18,10), (28, 11), (21, 18), (24, 28), (13, 23), (4, 28), (7, 18), (0, 11), (10, 10)]

        star()
        pygame.display.update()


    pygame.display.quit()
    pygame.quit()

def questao16():
    somatorio = 0
    print(somatorio)

