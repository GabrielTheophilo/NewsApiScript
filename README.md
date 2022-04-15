                                                                                                                  
<div align="center">
<h1> NewsApiScript</h1>

<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" height="25px;">
</div>
<p align="center"  style="text-align: justify;"><br>Este programa é feito para pesquisar diversos canais de notícias com uma palavra chave dada pelo usuário. Ele procura diversos sites como BBC, FoxNews, CBS e muitos outros. Instruções de uso abaixo
Este script consome a NewsApi para trazer diversas notícias de uma vez. Retorna um arquivo .txt com as notícias, links e informações. Ideal para pesquisas onde há a necessidade de pesquisar diversas fontes de uma vez</p>

<h3 align="center" > For english instructions, please access the <a href="https://github.com/GabrielTheophilo/NewsApiScript/blob/main/README-en.md">README-en.md</a> file</h3>




# Uso deste script

Este script requer python3.8 ou mais recente para rodar (compatibilidade não testada com versões abaixo)
Para checar os requisitos das bibliotecas, entre no arquivo [requirements.txt](https://github.com/GabrielTheophilo/NewsApiScript/blob/main/requirements.txt)

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

6 - Rode o newsapicript.py e siga os comandos do terminal

7 - Depois de rodar o código, um arquivo .json será criado com as informações e links sobre o tópico que você pesquisou. Abra com qualquer editor de texto ou IDE de sua preferência para acessar o arquivo .json.

