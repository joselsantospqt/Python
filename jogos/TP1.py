import turtle
import random
import math

# region RODAR
def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func
# endregion

def questao1():
    entrada = int(input('informe N:'))
    somatorio = 0

    for i in range(1, entrada + 1):
        if i % 2 == 0:
            somatorio += i

    print(somatorio)


def questao2():

    dias = int(input('informe dia:'))
    meses = int(input('informe mêses:'))
    anos = int(input('informe anos:'))

    qtd_dias = anos * 365 + meses * 30 + dias
    print(f'dias {qtd_dias}')


def questao3():

    entrada = int(input('informe N:'))
    if entrada < 0:
        print('nao da pra calcular')
        return


    fatorial = 1

    for i in range(entrada):
        fatorial *= i

    print(fatorial)

def questao4():

    entrada = int(input('informe N:'))
    if entrada < 0:
        print('nao da pra calcular')
        return

    fatorial = 1

    while entrada:
        fatorial *= entrada
        entrada -= 1

    print(fatorial)

def questao5():

    def num1(t, e):
        if e in t:
            return t.index(e)

    def num2(t):

        '''
        t1 = t[:int(len(t)/2)]
        t2 = t[int(t)/2:]
        '''

        t1 = t[:(len(t)//2)]
        t2 = t[int(t)//2:]

        print(t1)
        print(t2)
        return t1, t2


    def num3(t, e):
        if e in t:
            pos = t.index(e)
        return t[:pos] + t[pos + 1:]

    def num4(t):
        return t[::-1]

    def main():
        num1()
        num2()
        num3()
        num4()


    main()


def questao6():
    pass


def questao7():
    pass


def questao8():

    a = 6
    b = 5
    c = 12

    X = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    A = math.degrees(math.acos(X))

    Y = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    B = math.degrees(math.acos(Y))

    Z = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    C = math.degrees(math.acos(Z))


    turtle.left(360)
    turtle.speed('slowest')

    turtle.forward(a)
    turtle.left(180 - B)

    turtle.forward(c)
    turtle.left(180 - A)

    turtle.forward(b)

    turtle.Screen().exitonclick()

def questao10():
    lado = int(input('Digite N'))

    for i in range(4):
        turtle.forward(lado)
        turtle.lef(90)

    turtle.Screen().exitonclick()


def questao11():
    lado = int(input("Digite N"))

    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)

    turtle.Screen().exitonclick()

def questao12():
    raio = int(input('Digite N'))

    turtle.circle(raio)

    turtle.Screen().exitonclick()

def questao13():
    quantidadeQuadrados = int(input('Digite N quantidades'))

    turtle.speed('slowest')
    for i in range(quantidadeQuadrados):
        if i == 0:
            lado = 20
            for i in range(4):
                turtle.forward(lado)
                turtle.left(90)
        else:
            ladoNovo = lado + (i * 30)
            posicao = turtle.pos()
            turtle.penup()
            turtle.goto(posicao[0] - 15, posicao[1] - 15)
            turtle.pendown()
            for i in range(4):
                turtle.forward(ladoNovo)
                turtle.left(90)
    turtle.Screen().exitonclick()

def questao14():

    turtle.listen()

    turtle.onkey(questao10, 'q')
    turtle.onkey(questao11, 't')
    turtle.onkey(questao12, 'c')

    turtle.Screen().exitonclick()

def questao15():
    pass

def questao16():

    def randomPontos(i):
        return [(i, 0), (i, i), (0, i), (0, 0)]

    def desenhaPoligno(inicio, pontos, corLinha="black", corRecheio="white"):

        turtle.pencolor(corLinha)
        turtle.fillcolor(corRecheio)

        turtle.penup()

        turtle.goto(inicio)

        turtle.pendown()
        turtle.begin_fill()

        x, y = inicio

        for ponto in pontos:
            dx, dy = ponto
            turtle.goto(x + dx, y + dy)
        turtle.goto(inicio)

        turtle.end_fill()
        turtle.penup()

    def pinturas():

        quadrado = [(50, 0), (50, 50), (0,50), (0,0)]
        desenhaPoligno((200, 200), quadrado)

        quadro_secundario = randomPontos(100)
        desenhaPoligno((-200, 200), quadro_secundario, corLinha="green")

        triangulo = [(200, 0), (100, 100), (0,0)]
        desenhaPoligno((-200, -100), triangulo, corLinha="green")

        meuQuadrado = randomPontos(130)
        desenhaPoligno((-200, -100), meuQuadrado, corLinha="black", corRecheio="red")

    def main():
        pinturas
        turtle.done()


    main()



def questao17():

    palavra = input('Digite algo: ')
    numero = int(input('Digite um número: '))

    palavraCortada = palavra[:numero]
    restoPalavra = palavra[numero:]

    listaString = [restoPalavra + palavraCortada]

    print(listaString)

def questao18():

    lados = 5
    haste = 55
    angulo = 360 / lados


    turtle.left(360)

    for l in range(lados):
        turtle.forward(haste)
        turtle.back(haste)
        turtle.left(angulo)

    interno = (lados - 2) * 120
    externo = (180 - angulo) / 2


    turtle.forward(haste)
    turtle.left(180 - angulo)
    for l in range(lados):
        turtle.forward(haste)
        turtle.left(angulo)

    turtle.Screen().exitonclick()

@rodar
def questao19():

    numero = int(input('informe N:'))

    for i in range(numero):
        turtle.speed(10)
        turtle.color('red')
        turtle.forward(i*5)
        turtle.left(90)

    turtle.Screen().exitonclick()

def questao20():
    pass