# Arquivo que contém a lógica de separação do texto a partir do JSON recebido pela função principal(__init__ do módulo newsapiscript.py que faz requests a uma url e retorna um json)
# Classe >TxtParse< recebe os dados e a string de pesquisa do usuário e divide o json em dados, separados por categorias e organizados para serem "impressos" no arquivo final
# 
# ARQUIVOS DEPENDENTES: newsapiscript.py

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
            cdata += (f'DATA DA PESQUISA: {data_hoje.day}/{data_hoje.month}/{data_hoje.year}\n')
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
            FileWrite.OpenFileWriteTxt(query,cdata)
        except UnicodeEncodeError:
            print("Algum erro ocorreu durante a gravação em texto, o arquivo será gravado em .json")
            FileWrite.OpenFileWriteJson(query, jsondata)

    def jsonPrint(data, query):
        FileWrite.OpenFileWriteJson(query, data)
        
    def csvPrint(data, query):
        try:
            wdata = json.loads(data)
            jsondata=json.dumps(data)
            i = 0
            cdata = ''
            data_hoje = date.today()
            cdata += (f'DATA DA PESQUISA: {data_hoje.day}/{data_hoje.month}/{data_hoje.year},Site, Autor, Assunto,Link,Data\n')
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
               print(f"{a},{b},{c},{d},{e},{f},{g}\n")
               print("--------------------------------------")
               cdata += (f"{i},{a},{b},{c},{e},{f}\n")
            FileWrite.OpenFileWriteCsv(query,cdata)
        except UnicodeEncodeError:
            print("Algum erro ocorreu durante a gravação em texto, o arquivo será gravado em .json")
            FileWrite.OpenFileWriteJson(query, jsondata)

    
