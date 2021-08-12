# Arquivo principal(main) que coordena a execução do script. A requisição inicial é feita por meio deste script, que:
#                                                                                                                   1 - Chama a função PrintMenu para exibir opções iniciais para o usuário
#                                                                                                                   2 - Constrói a url de pesquisa do usuário e armazena na variável 
#                                                                                                                   3 - Faz a requisição para a Api
#                                                                                                                   4 - Guarda as respostas em variáveis(json_data>serializada; data>organizada em json identado)
#                                                                                                                   5 - Oferece ao usuário guardar os dados obtidos em texto ou json
#                                                                                                                   6 - Termina a execução do programa
#

import requests
import json
from apikey import ApiKey as ApiKey
from printmenu import PrintMenu
from txtParse import *
from stringurl import *

if __name__ == '__main__':
    PrintMenu.printMenu()
    url = StringUrl.__init__(StringUrl.StringAll(), StringUrl.StringSort(), StringUrl.LanguageQuery(), StringUrl.Query())
    print(url)
    response = requests.get(f'{url}')
    json_data = response.json()
    data = json.dumps(json_data, indent=4)
    escolha = str(input("Escolha uma saída para o arquivo --> txt(.txt) ou json(.json): ").lower())
    if escolha=='txt':
        TxtParse.txtPrint(data, StringUrl.query)
    elif escolha=='json':
        TxtParse.jsonPrint(data, StringUrl.query)
    PrintMenu.printEndMenu()
