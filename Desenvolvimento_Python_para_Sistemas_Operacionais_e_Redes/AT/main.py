import os

import psutil


def rodar(func):
    if __name__ == '__main__':
        print('-' * 10, func.__name__, '-' * 10)
        func()

    return func


def questao1():
    # Escreva um programa em Python que:
    # obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
    # imprima o nome do processo e seu PID;
    # imprima também o percentual de uso de CPU e de uso de memória.
    dados_processo = []
    CPU = psutil.cpu_percent(interval=None)
    memoria = psutil.virtual_memory().percent

    for proc in psutil.process_iter():
        dados_processo.append(proc)

    for i in dados_processo:
        print(f'PID:{i.pid} / NOME: {i.name()} ')

    print(f'Uso CPU:{CPU} / Uso Memória: {memoria} ')

    pass


def questao2():
    # Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
    entrada = input('Informe um nome para o arquivo')
    f = open(f'{entrada}.txt', 'w')
    f.write(' ')
    f.close()
    os.system(f"notepad.exe {entrada}.txt")


def questao3():

    # Escreva um programa em Python que:
    # gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco.
    # Obtenha o nome do diretório do usuário.
    # Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
    # gere um arquivo texto com os valores desta estrutura ordenados.

    lista = os.listdir()
    dic = {}
    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(os.stat(i).st_size)

    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    f = open('relatorio.txt', 'w')

    for x, y in dic:
        print(f'ARQUIVO: {x} / TAMANHO: {y} ')
        f.write(f'ARQUIVO: {x} / TAMANHO: {y}\n ')
    f.close()

    print(f'Diretório do usuário: {os.environ["HOMEPATH"]}')

@rodar
def questao4():
    # Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
    # arquivo.txt
    # Bom dia
    # Você pode falar agora?
    # Resultado na tela:
    # ?aroga ralaf edop êcoV
    # aid moB

    def reverter(x):
        return x[::-1]


    f = open('relatorio.txt', 'r')

    for x in f:
      txt = reverter(x)
      print(txt)



    pass


def questao5():
    #Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
    #a.txt
    #1 15 -42 33 -7 -2 39 8
    # b.txt
    #19 56 -43 23 -7 -11 33 21 61 9
    #Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela. Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.


    pass


def questao6():
    # Escreva um programa cliente e servidor sobre TCP em Python em que:
    # O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
    # O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.

    pass


def questao7():
    # Escreva um programa cliente e servidor sobre UDP em Python que:
    # O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
    # O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.

    pass


def questao8():
    # Escreva 3 programas em Python que resolva o seguinte problema:
    # Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
    # Para calcular o fatorial, utilize a seguinte função:
    # Os modos de desenvolver seu programa devem ser:
    # sequencialmente (sem concorrência);
    # usando o módulo threading com 4 threads;
    # usando o módulo multiprocessing com 4 processos.

    pass


def questao9():
    # Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos. Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes).
    # Obs.: Para testar, crie um vetor com apenas um número relativamente grande (10, por exemplo) ou use a função random para gerar um vetor com números aleatórios. Cuidado ao usar números muito grandes, pois o fatorial pode resultar em um valor que o computador não consiga representar por falta de precisão.

    pass
