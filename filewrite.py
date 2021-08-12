# Arquivo que contém a lógica de escrita dos arquivos, dividido em duas classes ( -> FolderWrite <- | -> FileWrite <- )
#
# Classe >FolderWrite< não recebe input, é chamada para criar uma pasta no desktop do usuário para armazenar os arquivos que serão gerados
#
# Classe >FileWrite< recebe input (str,*args)  
#                                  no qual (str) equivale á string de pesquisa do usuário(para nomear o arquivo de acordo com a pesquisa feita)
#                                  e (*args) equivale aos dados extraídos do arquivo JSON, que foram parseados pelo módulo txtparse e serão escritos dentro do arquivo
# 
# ARQUIVOS DEPENDENTES -> txtParse.py

import os
import os.path

class FolderWrite:
    def FolderWrite():
        username = os.getlogin()
        try:
            os.mkdir(f'C:\\Users\\{username}\\Desktop\\NewsApiScript')
            return 0
            
        except:
            print("Pasta já existente na área de trabalho")
            return 1

class FileWrite:
    def OpenFileWriteJson(str,*args):
        username = os.getlogin()
        
        folder = FolderWrite.FolderWrite()
        if folder == 0:
            path = (f'C:\\Users\\{username}\\Desktop\\NewsApiScript')
        if folder == 1:
            try:
                path = (f'C:\\Users\\{username}\\Desktop\\NewsApiScript')
            except:
                path = (f'C:\\Users\\{username}\\Desktop')
        
        try:
            file = open(f'{path}\\{str}.json', 'x')
            file.write(*args)
            file.close()

        except:
            file = open(f'{path}\\{str}.json', 'a')
            file.write(*args)
            file.close()

    def OpenFileWriteTxt(str,*args):
        username = os.getlogin()
        
        folder = FolderWrite.FolderWrite()
        if folder == 0:
            path = (f'C:\\Users\\{username}\\Desktop\\NewsApiScript')
        if folder == 1:
            try:
                path = (f'C:\\Users\\{username}\\Desktop\\NewsApiScript')
            except:
                path = (f'C:\\Users\\{username}\\Desktop')
        
        try:
            file = open(f'{path}\\{str}.txt', 'x')
            file.write(*args)
            file.close()

        except:
            file = open(f'{path}\\{str}.txt', 'a')
            file.write(*args)
            file.close()
