<h1 align="center"> ✅NewsApiScript✅</h1>
<p align="center">Este programa é feito para pesquisar diversos canais de notícias com uma palavra chave dada pelo usuário. Ele procura diversos sites como BBC, FoxNews, CBS e muitos outros. Instruções de uso abaixo</p>
<p align="center">Script para uso pessoal do endpoint do NewsApi. Retorna um arquivo .json como especificado pela documentação do newsApi</p>

ooooo      ooo                                      .oooooo..o                     o8o                 .         .o.                   o8o  
`888b.     `8'                                     d8P'    `Y8                     `"'               .o8        .888.                  `"'  
 8 `88b.    8   .ooooo.  oooo oooo    ooo  .oooo.o Y88bo.       .ooooo.  oooo d8b oooo  oo.ooooo.  .o888oo     .8"888.     oo.ooooo.  oooo  
 8   `88b.  8  d88' `88b  `88. `88.  .8'  d88(  "8  `"Y8888o.  d88' `"Y8 `888""8P `888   888' `88b   888      .8' `888.     888' `88b `888  
 8     `88b.8  888ooo888   `88..]88..8'   `"Y88b.       `"Y88b 888        888      888   888   888   888     .88ooo8888.    888   888  888  
 8       `888  888    .o    `888'`888'    o.  )88b oo     .d8P 888   .o8  888      888   888   888   888 .  .8'     `888.   888   888  888  
o8o        `8  `Y8bod8P'     `8'  `8'     8""888P' 8""88888P'  `Y8bod8P' d888b    o888o  888bod8P'   "888" o88o     o8888o  888bod8P' o888o 
                                                                                         888                                888             
                                                                                        o888o                              o888o            
                                                                                                                                            


# Uso deste script
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


