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