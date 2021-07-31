
<h1 align="center"> NewsApiScript</h1>
<p align="center">This program is intended to be used for searching several news sites at once with an user-provided keyword. It searches through several sites like BBC, CBS, FoxNews and many others. Instructions as follows</p>
<p align="center">This script uses the NewsApi to return several news articles at once. It returns a .txt file with the news, links and additional information. Ideal for research where a large number of articles about a topic are needed.</p>

<h2 align="center">Para instruções em PT-BR, acessar o README-ptBr.md</h2>

# Use of this script

This program requires Python 3.x.x to run

1 - To use this python script you need to clone the repository: 
```bash
git clone https://github.com/GabrielTheophilo/NewsApiScript.git
```
2 - CD into the directory and install the required libraries with python:
```bash
python -m pip install requirements.txt
```
3 - Open the folder that you just cloned

4 - Register a ApiKey for your personal use at [NewsApi](https://newsapi.org/)

5 - Open the apikey.py file and add the 32 charachter code after the 'apikey=', i.e 'apikey=YOURAPIKEY_HERE'

6 - Run the newsapiscript.py and follow the CLI commands

IMPORTANT: If you have the free plan on the newsapi website, your search will be limited to ONE page, so when the program asks for the number of pages, make sure to specify "1", or else the API will return an error, with the code "maximumResultsReached".

7 - After you run the code, a .json file will be created with the information and links about the news you searched for. Open with any text editor or IDE of your choosing to access the .json information.



