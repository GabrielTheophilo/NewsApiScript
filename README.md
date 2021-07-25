<h1 align="center"> NewsApiScript</h1>
<p align="center">Script for personal use of the NewsApi endpoint. Returns a json file as specified in the docs of the newsApi</p>

<p align="center">Para instruções em PT-BR, acessar o README-ptBr.md</p>

# Use of this script
To use this python script you need to clone the repository: 
```bash
git clone https://github.com/GabrielTheophilo/NewsApiScript.git
```

Open the folder that you just cloned

Register a ApiKey for your personal use at [NewsApi](https://newsapi.org/)

Open the apikey.py file and add the 32 charachter code after the 'apikey=', i.e 'apikey=YOURAPIKEY_HERE'

Run the newsscript.py and follow the CLI commands

IMPORTANT: If you have the free plan on the newsapi website, your search will be limited to ONE page, so when the program asks for the number of pages, make sure to specify "1", or else the API will return an error, with the code "maximumResultsReached".

After you run the code, a .json file will be created with the information and links about the news you searched for. Open with any text editor or IDE of your choosing to access the .json information.


