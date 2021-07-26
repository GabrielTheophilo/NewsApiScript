import requests
import json
from apikey import ApiKey as ApiKey

#
# Em construção
#
# Para fazer: 
# 1 - Organizar as querys em funções para melhorar a organização do código
# 2 - Definir istruções apenas em português ou em inglês
#

def printMenu():
    #Main menu to output status choices to users
    print("Quais notícias estarão na sua pesquisa?")
    print("---------------------------------------")
    print("1 - Top Headlines")
    print("2 - Tudo")
    print("3 - Sair")
    
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

# while True is an infinite loop because every option breaks the program or asks again for user input
# If user input is valid, the program runs and breaks (even if the request is unsuccessful)

while True:
    printMenu()                                             # PRINT MAIN MENU
    status = int(input("\nSua escolha: "))                  # Asks for user input
    if status < 1 or status>3:                              # Checks ir user input is invalid
        print("Selecione uma opção válida")                 # If user input is invalid, it will run the inicial input again
        status = int(input("\n Sua escolha: "))
    elif status == 1:                                       # If user input is valid, and the user wants to search the top-headlines of an subjetct, run the block below
        url1 = ('https://newsapi.org/v2/top-headlines?')
        print("Selecione o termo que deseja pesquisar: ")   # Input of the query string
        query = str(input(''))
        query1 = (f'q={query}&')
        apiKey = (ApiKey.key)
        print("Gostaria de pesquisar globalmente ou apenas notícias em canais brasileiros?")
        br = str(input("").lower())
        if br=="brasil" or br=="brasileiros" or br=="brazil":
            countryQuery = ('country=br&')
            response = requests.get(url1+countryQuery+query1+apiKey)         # GET request to url
            json_data = response.json()                         # GET response as json being stored in json_data variable
            data = json.dumps(json_data, indent=4)              # json output and parsing with indent
            file = OpenFileWrite(query, data)                   
            print (data)
            break
        else:
            response = requests.get(url1+query1+apiKey)         # GET request to url
            json_data = response.json()                         # GET response as json being stored in json_data variable
            data = json.dumps(json_data, indent=4)              # json output and parsing with indent
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
        print("Deseja receber notícias somente em português?")
        language = str(input("").lower())
        if language=="sim":
            languageQuery = ('language=pt&')
            print("Deseja ordenar por relevância ou popularidade? Escreva abaixo")
            sort = str(input("".lower()))
            if sort=="relevância":
                sortQuery = ('sortBy=relevancy&')
                response = requests.get(url1+query1+languageQuery+sortQuery+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break
            elif sort=="popularidade":
                sortQuery = ('sortBy=popularity&')
                response = requests.get(url1+query1+languageQuery+sortQuery+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break
            else:
                response = requests.get(url1+query1+languageQuery+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break
        else: 
            print("Deseja ordenar por relevância ou popularidade? Escreva abaixo")
            sort = str(input("".lower()))
            if sort=="relevância":
                sortQuery = ('sortBy=relevancy&')
                response = requests.get(url1+query1+sortQuery+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break
            elif sort=="popularidade":
                sortQuery = ('sortBy=popularity&')
                response = requests.get(url1+query1+sortQuery+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break       
            else:
                response = requests.get(url1+query1+query2+apiKey)
                json_data = response.json()
                data = json.dumps(json_data, indent=4)
                file = OpenFileWrite(query, data)
                print (data)
                break

    elif status == 3:
        break
