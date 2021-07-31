import requests
import json
from apikey import ApiKey as ApiKey

def printMenu():
    #Main menu to output status choices to users
    print(r''' _   _                      _          _ ____            _       _   
| \ | | _____      _____   / \   _ __ (_) ___|  ___ _ __(_)_ __ | |_ 
|  \| |/ _ \ \ /\ / / __| / _ \ | '_ \| \___ \ / __| '__| | '_ \| __|
| |\  |  __/\ V  V /\__ \/ ___ \| |_) | |___) | (__| |  | | |_) | |_ 
|_| \_|\___| \_/\_/ |___/_/   \_\ .__/|_|____/ \___|_|  |_| .__/ \__|
                                |_|                       |_|        '''
    )
    print("Quais notícias estarão na sua pesquisa?")
    print("---------------------------------------")
    print("Top Headlines")
    print("Tudo")
    print("---------------------------------------")
    
    
def OpenFileWrite(str, *args):
    try:
        file = open(f'{str}.txt', 'x')
        file.write(*args)
        file.close()
        
    except:
        file = open(f'{str}.txt', 'a')
        file.write(*args)
        file.close()

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
        elif StringSort == '3':
            pass
        
        if LanguageQuery == '1':
            StringUrl.url += StringUrl.language
        elif LanguageQuery == '':
            pass
        
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
    wdata = json.loads(data)
    i = 0 
    for x in wdata['articles'][i]:
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
       cdata = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n\n\n\n\n")
       file = OpenFileWrite(StringUrl.query, cdata)
    print (data)