import os
import os.path
class FileWrite:
    def OpenFileWriteJson(str,*args):
        username = os.getlogin()

        try:
            file = open(f'C:\\Users\\{username}\\Desktop\\{str}.json', 'x')
            file.write(*args)
            file.close()

        except:
            file = open(f'C:\\Users\\{username}\\Desktop\\{str}.json', 'a')
            file.write(*args)
            file.close()

    def OpenFileWriteTxt(str,*args):
        username = os.getlogin()
        try:
            file = open(f'C:\\Users\\{username}\\Desktop\\{str}.txt', 'x')
            file.write(*args)
            file.close()

        except:
            file = open(f'C:\\Users\\{username}\\Desktop\\{str}.txt', 'a')
            file.write(*args)
            file.close()
