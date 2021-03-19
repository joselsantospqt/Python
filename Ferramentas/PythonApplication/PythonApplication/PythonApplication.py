import os
import re
from PyPDF2 import PdfFileWriter, PdfFileReader

def busca_arquivo_rec(dir):
    lista_dir = []
    lista_resp = []
    lista_dir.append(dir)

    while lista_dir:
        dir_atual = lista_dir[0]
        l = []
        try:
            l = os.listdir(dir_atual)
        except:
            pass
        for i in l:
            arq = os.path.join(dir_atual, i)
            os.path.isfile(arq)
            filename, file_extension = os.path.splitext(i)
            if os.path.isfile(arq):
                if file_extension == '.pdf':
                    lista_resp.append(arq)
            elif os.path.isdir(arq):
                lista_dir.append(arq)
        lista_dir.remove(dir_atual)
    return (lista_resp)

def main(lista_arquivos, dir):

    with open('relatorio.txt', 'w') as arquivo:
        for i in lista_arquivos:
            arquivo.write('ARQUIVOS ENCONTRADOS PDFS ENCONTRADOS:\n')
            arquivo.write(f'{i}\n')

        for i in lista_arquivos:
            inputpdf = PdfFileReader(open(i, "rb"))
            filename, file_extension = os.path.splitext(i)
            lenRounter = len(dir) + 2
            lenFile = len(filename)
            filename = filename[lenRounter:lenFile]
            destination_directory = filename.replace("/", "\\")
            try:
                if os.path.isdir(destination_directory):
                    pass
                else:
                    os.mkdir(destination_directory)

                if inputpdf.numPages >= 2:
                    for i in range(inputpdf.numPages):
                        output = PdfFileWriter()
                        output.addPage(inputpdf.getPage(i))
                        output_filename = os.path.join(destination_directory, '{}_page_{}.pdf'.format(filename, i))
                        with open(output_filename, "wb") as outputStream:
                            output.write(outputStream)
                            arquivo.write('\nGRAVADO COM SUCESSO:\n')
                            arquivo.write(f'-Nome:{filename}_page_{i}.pdf\n-Pasta:{destination_directory}\n')

            except AssertionError as e:
                arquivo.write('\nERRO AO GRAVAR:\n')
                arquivo.write(f'-Nome do arquivo:{filename}\n-Pasta:{destination_directory}\n')
                print(e)

            except OSError:
                print("Creation of the directory %s failed" % destination_directory)
            else:
                print("Successfully created the directory %s " % destination_directory)


if __name__ == '__main__':
    #dir = os.environ['HOMEPATH'] + '\\PDF'

    dir = input('Entre com caminho:')

    lista_arquivos = busca_arquivo_rec(dir)

main(lista_arquivos, dir)
