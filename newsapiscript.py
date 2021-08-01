import requests
import json
from apikey import ApiKey as ApiKey
from printmenu import PrintMenu
import os.path
import os

def printMenu():
    #Main menu to output status choices to users
    PrintMenu.__init__()
    print("Quais notícias estarão na sua pesquisa?")
    print("---------------------------------------")
    print("Top Headlines")
    print("Tudo")
    print("---------------------------------------")
    
    
def OpenFileWriteJson(str,*args):
    username = os.getlogin()
    
    try:
        file = open(f'C:\\Users\\{username}\\Desktop\\{str}.json', 'x')
        file.write(*args)
        file.close()
        
    except:
        file = open(f'C:\\Users\\{username}\\Desktop\\{str}.json' 'a')
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

def txtPrint(data, query):
    wdata = json.loads(data)
    i = 0
    cdata = ''
    for x in wdata['articles']:
       print(i)
       a = wdata['articles'][i]['source']['name']
       b = wdata['articles'][i]['author']
       c = wdata['articles'][i]['title']
       d = wdata['articles'][i]['description']
       e = wdata['articles'][i]['url']
       f = wdata['articles'][i]['publishedAt']
       g = wdata['articles'][i]['content']
       i += 1
       print(f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n")
       print("--------------------------------------")
       cdata += (f"TEXTO{i}\n\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n\n\n\n\n")
    file = OpenFileWriteTxt(query,cdata)

def jsonPrint(data, query):
    file = OpenFileWriteJson(query, data)
    

class StringUrl(ApiKey):
    key = ApiKey.key
    urlTop = 'https://newsapi.org/v2/top-headlines?'
    urlAll = 'https://newsapi.org/v2/everything?'
    pagesize = 'pageSize=100&'
    country = 'country=br&'
    language =  'language=pt&'
    popularity = 'sortBy=relevancy&'
    relevancy = 'sortBy=popularity&'
    url = ''
    query = ''
    def __init__(StringAll, StringSort,LanguageQuery, Query):
        if StringAll == '1' or StringAll == '':
            StringUrl.url += StringUrl.urlAll
        else:
            StringUrl.url += StringUrl.urlTop
            
        if StringSort == '1' or StringSort == '':
            StringUrl.url += StringUrl.relevancy
        elif StringSort == '2':
            StringUrl.url += StringUrl.popularity

        if LanguageQuery == '1':
            StringUrl.url += StringUrl.language
        StringUrl.url += (f'q={Query}&')
        StringUrl.url += StringUrl.pagesize
        StringUrl.url += StringUrl.key
        StringUrl.query += Query
        
        return StringUrl.url

        
    def StringAll():
        return str(input('Deseja ver todas as notícias ou apenas as Top-Headlines? || 1 para Todas, 2 para Principais: '))
    
    def StringSort():
        return str(input('Deseja ordernar sua busca? || Digite 1 para Relevância, 2 para Popularidade, 3 para não ordernar: '))

    def Query():
        return str(input("Selecione o termo que deseja pesquisar: "))
    
    def LanguageQuery():
        return str(input("Deseja receber notícias apenas em português ou todas? || 1 para Português, 2 para Todas: "))
    def ApiKey():
        return str(ApiKey.key)
        
if __name__ == '__main__':
    printMenu()
    url = StringUrl.__init__(StringUrl.StringAll(), StringUrl.StringSort(), StringUrl.LanguageQuery(), StringUrl.Query())
    print(url)
    response = requests.get(f'{url}')
    json_data = response.json()
    data = json.dumps(json_data, indent=4)
    escolha = str(input("Escolha uma saída para o arquivo --> txt(.txt) ou json(.json): ").lower())
    if escolha=='txt':
        txtPrint(data, StringUrl.query)
    elif escolha=='json':
        jsonPrint(data, StringUrl.query)
    print ("Programa finalizado, seu arquivo foi gerado na Área de Trabalho")
    print("*Aperte qualquer tecla para sair*")
    str(input(""))