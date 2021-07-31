<h1 align="center"> NewsApiScript</h1>
<p align="center">Este programa é feito para pesquisar diversos canais de notícias com uma palavra chave dada pelo usuário. Ele procura diversos sites como BBC, FoxNews, CBS e muitos outros. Instruções de uso abaixo</p>
<h2 align="center">Este script consome a NewsApi para trazer diversas notícias de uma vez. Retorna um arquivo .txt com as notícias, links e informações. Ideal para pesquisas onde há a necessidade de pesquisar diversas fontes de uma vez</h2>

<h3 align="center"> For english instructions, access the README-en.md file</h3>

<h2> PARA BAIXAR ESSE SCRIPT COMO .EXE E RODAR NO SEU COMPUTADOR, ENTRE NESTE [REPOSITÓRIO](https://github.com/GabrielTheophilo/NewsApiScript.exe)


# Uso deste script

No momento, este script precisa de Python 3 para rodar (e a biblioteca adicional requests, que pode ser baixada ao rodar o requirements.txt)

1 - Para usar esse script python primeiramente você precisa clonar o repositório: 
```bash
git clone https://github.com/GabrielTheophilo/NewsApiScript.git
```

2 - Dê um CD no directory e instale as bibliotecas que vamos usar em python:
```bash
python -m pip install requirements.txt
```

3 - Abra a pasta que você clonou

4 - Registre uma chave para a API no site [NewsApi](https://newsapi.org/)

5 - Abra o arquivo apikey.py e adicione a chave de 32 caracteres após o 'apikey=', exemplo: 'apikey=SUACHAVEAQUI'

6 - Rode o newsscript.py e siga os comandos do terminal

IMPORTANTE: Se você tem o plano gratuito da API, sua pesquisa estará limitada a uma página, então quando o programa pedir o número de páginas da sua busca, por favor especifique como "1", ou a API retornará um erro após imprimir a primeira página, com o código "maximumResultsReached".

7 - Depois de rodar o código, um arquivo .json será criado com as informações e links sobre o tópico que você pesquisou. Abra com qualquer editor de texto ou IDE de sua preferência para acessar o arquivo .json.

