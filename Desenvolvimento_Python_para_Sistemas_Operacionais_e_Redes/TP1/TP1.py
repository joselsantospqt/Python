import os
import datetime
import psutil
import subprocess
import time


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

@rodar
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

def questao11():
    print(subprocess.run(["notepad", "texto.txt"]))

def questao12():
    subprocess.run(["notepad"])
    print('SubProcess - NotedPad')

    os.system("notepad")
    print("OS - NotedPad")


def questao13():
    p = subprocess.Popen(["notepad", "arq_texto.txt"])
    print("PID do processo criado:", p.pid)


def questao14():
    '''A função psutil.process_iter() é equivalente a psutil.pids().
       Ela retorna a lista de processos que estão executando na máquina.
       A diferença está na forma como é implementada, de modo que seja
       mais eficiente quando executado repetidamente (em iterações).'''

def questao15():
    lista = psutil.pids()

    for pid in lista:
        if pid > 4:
            p = psutil.Process(pid)
            print(f"{p.name()}, {p.create_time()}, {p.memory_info()}")


def questao16():

    p = psutil
    def temporizador(p, interval=0.1):
        for i in range(len(psutil.cpu_times_percent(percpu=True))):
            print(p.cpu_times(interval))
    temporizador(p)

def questao17():
    p = psutil
    for i in range(20):
        print(psutil.cpu_times_percent(interval=1))


def questao18():
    print(f'memoria = {str(psutil.virtual_memory().total**10)[:2]} GB')
    print(f'swap = {str(psutil.swap_memory().total**10)[:2]} GB')


def questao19():
    print(psutil.disk_usage(path='C:').free)


def questao20():
    p = psutil.disk_partitions()
    print(f'dispositivo = {p[0].device}')
    print(f'sistema  = {p[0].fstype}')
    print(f'total de armazenamento = {psutil.disk_usage(path="C:").total}')
    print(f'armazenamento disponível = {psutil.disk_usage(path="C:").free}')
