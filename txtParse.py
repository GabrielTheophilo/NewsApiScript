import json
from datetime import date
from filewrite import *

class TxtParse:
    def txtPrint(data, query):
        try:
            wdata = json.loads(data)
            jsondata=json.dumps(data)
            i = 0
            cdata = ''
            data_hoje = date.today()
            cdata += (f'DATA DA PESQUISA: {data_hoje.day}/{data_hoje.month}/{data_hoje.year}')
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
            file = FileWrite.OpenFileWriteTxt(query,cdata)
        except UnicodeEncodeError:
            print("Algum erro ocorreu durante a gravação em texto, o arquivo será gravado em .json")
            FileWrite.OpenFileWriteJson(query, jsondata)

    def jsonPrint(data, query):
        file = FileWrite.OpenFileWriteJson(query, data)
