import requests
import json
from apikey import ApiKey as ApiKey

def printMenu():
    #Main menu to output status choices to users
    print("Quais notícias estarão na sua pesquisa?")
    print("---------------------------------------")
    print("Top Headlines")
    print("Tudo")
    print("Aperte 3 para Sair")
    
def OpenFileWrite(str, *args):
    #Function to write a file with the name of the user's query
    # 1º block -> Create file, write and close
    # 2º block -> Open existing file, write and close
    try:
        file = open(f'{str}.json', 'x')
        file.write(*args)
        file.close()
        
    except:
        file = open(f'{str}.json', 'a')
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
        if StringAll == '1':
            StringUrl.url += StringUrl.urlAll
        else:
            StringUrl.url += StringUrl.urlTop
            
        if StringSort == '1':
            StringUrl.url += StringUrl.relevancy
        elif StringSort == '2':
            StringUrl.url += StringUrl.popularity
        
        if LanguageQuery == '1':
            StringUrl.url += StringUrl.language
        
        query = Query
        StringUrl.query += query
        query1 = (f'q={query}&')
        StringUrl.url += query1
        StringUrl.url += StringUrl.ApiKey()
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
    url = StringUrl.__init__(StringUrl.StringAll(), StringUrl.StringSort(), StringUrl.LanguageQuery(), StringUrl.Query())
    print(url)
    response = requests.get(f'{url}')
    json_data = response.json()
    data = json.dumps(json_data, indent=4)
    file = OpenFileWrite(StringUrl.query, data)
    print (data)
