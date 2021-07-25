import requests
import json
from apikey import ApiKey as ApiKey

def printMenu():
    print("Quais notícias estarão na sua pesquisa?")
    print("---------------------------------------")
    print("1 - Top Headlines")
    print("2 - Tudo")
    print("3 - Sair")
    
def OpenFileWrite(str, *args):
    try:
        arq = open(f'{str}.json', 'x')
        arq.write(*args)
        arq.close()
        
    except:
        arq = open(f'{str}.json', 'a')
        arq.write(*args)
        arq.close()


while True:
    printMenu()
    status = int(input("\nSua escolha: "))
    if status < 1 or status>3:
        print("Selecione uma opção válida")
        status = int(input("\n Sua escolha: "))
    elif status == 1: 
        url1 = ('https://newsapi.org/v2/top-headlines?')
        print("Selecione o termo que deseja pesquisar: ")
        query = str(input(''))
        query1 = (f'q={query}&')
        apiKey = (ApiKey.key)
        response = requests.get(url1+query1+apiKey)
        json_data = response.json()
        data = json.dumps(json_data, indent=4)
        file = OpenFileWrite(query, data)

        print (data)
        break
    elif status == 2: 
        url1 = ('https://newsapi.org/v2/everything?')
        print("Selecione o termo que deseja pesquisar: ")
        query = str(input(''))
        query1 = (f'q={query}&')
        query2 = ('pageSize=100&')
        apiKey = (ApiKey.key)
        
        print("Quantas páginas de resultados deseja procurar?")
        pageNum = int(input(""))
        while pageNum<=0 or pageNum>=50:
            print("Escolha inválida, por favor mantenha o pedido entre 1 e 50 páginas")
            pageNum = int(input("Insira o número de páginas"))
        if pageNum == 1:
            response = requests.get(url1+query1+query2+apiKey)
            json_data = response.json()
            data = json.dumps(json_data, indent=4)
            file = OpenFileWrite(query, data)
            print (data)
            break
        else:
            for x in range(1, pageNum):
                pageNumero = (f'page={x}&')
                response = requests.get(url1+query1+query2+pageNumero+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
            
            

    elif status == 3:
        break
