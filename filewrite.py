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
