import os
import datetime
import psutil


def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func

def questao1():
    nome = os.getlogin()
    print(nome)

def questao2():
    "a - São chaves com valores e cada uma delas é representada em um dicionário"

    key = os.environ
    print(key)
    "print(os.environ['USERNAME'])"

    print(os.environ['USERPROFILE'])

def questao3():

    pid = os.getpid()
    print(pid)

def questao4():
    caminho_Absoluto = os.getcwd()
    print(caminho_Absoluto)

def questao5():
    arquivo = "texto.txt"
    if os.path.exists(arquivo):
        print(arquivo, "existe !")
    else:
        print(arquivo, "Não existe !")

def questao6():
    arquivo = "texto.txt"
    caminho_Absoluto = os.getcwd()
    extension = os.path.splitext(arquivo)[0]
    print(extension)


def questao7():
    caminho_Absoluto = os.getcwd()
    arquivo = "C:\\Users\\José Ricardo\\Documents\Python\\Desenvolvimento Python para Sistemas Operacionais e Redes\\texto.txt"
    print(os.path.dirname((arquivo)))


def questao8():
    lista = os.listdir()
    caminho_Absoluto = os.getcwd() + "\\"
    for i in lista:
        print("Arquivo: " + i)
        print(os.stat(caminho_Absoluto + i).st_size)


def questao9():
    lista = os.listdir()
    caminho_Absoluto = os.getcwd() + "\\"
    for i in lista:
        print("Arquivo: " + i)
        print(os.stat(caminho_Absoluto + i).st_size)
        print("Data de Criação:")
        print(datetime.datetime.fromtimestamp(os.stat(caminho_Absoluto + i).st_ctime))
        print("Data de modificação :")
        print(datetime.datetime.fromtimestamp(os.stat(caminho_Absoluto + i).st_mtime))

def questao10():
    "A diferença os.exec apenas inicia um processo sem retornar nada ao processo chamador."
    "A diferença está nos primeiro e último argumentos de os.spawnv."
    "O primeiro argumento indica que é para esperar o processo terminar"
    " antes de retornar ao processo que criou."
@rodar
def questao11():
 
def questao12():
    print('teste')

def questao13():
    print('teste')

def questao14():
    print('teste')

def questao15():
    print('teste')

def questao16():
    print('teste')

def questao17():
    print('teste')

def questao18():
    print('teste')

def questao19():
    print('teste')

def questao20():
    print('teste')
