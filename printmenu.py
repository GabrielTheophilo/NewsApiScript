# Arquivo que contém os menus para interação na linha de comando do terminal
# Classe >PrintMenu< contém as artes que irão compor o menu e, também, os outros menus para auxiliar o usuário na pesquisa
# 
# ARQUIVOS DEPENDENTES: newsapiscript.py

class PrintMenu():
    a = (r'''ooooo      ooo                                           .o.                   o8o   .oooooo..o                     o8o                 .   
`888b.     `8'                                          .888.                  `"'  d8P'    `Y8                     `"'               .o8   
 8 `88b.    8   .ooooo.  oooo oooo    ooo  .oooo.o     .8"888.     oo.ooooo.  oooo  Y88bo.       .ooooo.  oooo d8b oooo  oo.ooooo.  .o888oo 
 8   `88b.  8  d88' `88b  `88. `88.  .8'  d88(  "8    .8' `888.     888' `88b `888   `"Y8888o.  d88' `"Y8 `888""8P `888   888' `88b   888   
 8     `88b.8  888ooo888   `88..]88..8'   `"Y88b.    .88ooo8888.    888   888  888       `"Y88b 888        888      888   888   888   888   
 8       `888  888    .o    `888'`888'    o.  )88b  .8'     `888.   888   888  888  oo     .d8P 888   .o8  888      888   888   888   888 . 
o8o        `8  `Y8bod8P'     `8'  `8'     8""888P' o88o     o8888o  888bod8P' o888o 8""88888P'  `Y8bod8P' d888b    o888o  888bod8P'   "888" 
                                                                    888                                                   888               
                                                                   o888o                                                 o888o              
                                                                                                                                         ''')
    b = (r'''888b    888                                        d8888          d8b  .d8888b.                   d8b          888    
8888b   888                                       d88888          Y8P d88P  Y88b                  Y8P          888    
88888b  888                                      d88P888              Y88b.                                    888    
888Y88b 888  .d88b.  888  888  888 .d8888b      d88P 888 88888b.  888  "Y888b.    .d8888b 888d888 888 88888b.  888888 
888 Y88b888 d8P  Y8b 888  888  888 88K         d88P  888 888 "88b 888     "Y88b. d88P"    888P"   888 888 "88b 888    
888  Y88888 88888888 888  888  888 "Y8888b.   d88P   888 888  888 888       "888 888      888     888 888  888 888    
888   Y8888 Y8b.     Y88b 888 d88P      X88  d8888888888 888 d88P 888 Y88b  d88P Y88b.    888     888 888 d88P Y88b.  
888    Y888  "Y8888   "Y8888888P"   88888P' d88P     888 88888P"  888  "Y8888P"   "Y8888P 888     888 88888P"   "Y888 
                                                         888                                          888             
                                                         888                                          888             
                                                         888                                          888           ''')
    c = (r'''       ___       __        __     __   __   __     __  ___ 
|\ | |__  |  | /__`  /\  |__) | /__` /  ` |__) | |__)  |  
| \| |___ |/\| .__/ /~~\ |    | .__/ \__, |  \ | |     |  
                                                          ''')
    d = (r'''888888ba                                .d888888           oo .d88888b                    oo            dP   
88    `8b                              d8'    88              88.    "'                                 88   
88     88 .d8888b. dP  dP  dP .d8888b. 88aaaaa88a 88d888b. dP `Y88888b. .d8888b. 88d888b. dP 88d888b. d8888P 
88     88 88ooood8 88  88  88 Y8ooooo. 88     88  88'  `88 88       `8b 88'  `"" 88'  `88 88 88'  `88   88   
88     88 88.  ... 88.88b.88'       88 88     88  88.  .88 88 d8'   .8P 88.  ... 88       88 88.  .88   88   
dP     dP `88888P' 8888P Y8P  `88888P' 88     88  88Y888P' dP  Y88888P  `88888P' dP       dP 88Y888P'   dP   
                                                  88                                         88              
                                                  dP                                         dP             ''')
    e = (r'''    _   __                  ___          _ _____           _       __ 
   / | / /__ _      _______/   |  ____  (_) ___/__________(_)___  / /_
  /  |/ / _ \ | /| / / ___/ /| | / __ \/ /\__ \/ ___/ ___/ / __ \/ __/
 / /|  /  __/ |/ |/ (__  ) ___ |/ /_/ / /___/ / /__/ /  / / /_/ / /_  
/_/ |_/\___/|__/|__/____/_/  |_/ .___/_//____/\___/_/  /_/ .___/\__/  
                              /_/                       /_/           ''')
    f = (r'''███╗   ██╗███████╗██╗    ██╗███████╗ █████╗ ██████╗ ██╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
████╗  ██║██╔════╝██║    ██║██╔════╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗███████║██████╔╝██║███████╗██║     ██████╔╝██║██████╔╝   ██║   
██║╚██╗██║██╔══╝  ██║███╗██║╚════██║██╔══██║██╔═══╝ ██║╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
██║ ╚████║███████╗╚███╔███╔╝███████║██║  ██║██║     ██║███████║╚██████╗██║  ██║██║██║        ██║   
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                                                                                   ''')
    
    def __init__():
        import random
        random1 = random.randint(0,5)
        if random1==0:
            print(PrintMenu.a)
        if random1==1:
            print(PrintMenu.b)
        if random1==2:
            print(PrintMenu.c)
        if random1==3:
            print(PrintMenu.d)
        if random1==4:
            print(PrintMenu.e)
        if random1==5:
            print(PrintMenu.f)
            
    def Menu():
        #Main menu to output status choices to users
        PrintMenu.__init__()
        print("Quais notícias estarão na sua pesquisa?")
        print("---------------------------------------")
        print("Top Headlines")
        print("Tudo")
        print("---------------------------------------")
    
    def EndMenu():
        print ("Programa finalizado, seu arquivo foi gerado na Área de Trabalho")
        print("*Aperte qualquer tecla para sair*")
        str(input(""))
        
if __name__=='__main__':
    PrintMenu.Menu()
    
    
    
