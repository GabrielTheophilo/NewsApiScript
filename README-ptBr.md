<h1 align="center"> NewsApiScript</h1>
<p align="center">Script para uso pessoal do endpoint do NewsApi. Retorna um arquivo .json como especificado pela documentação do newsApi</p>


# Uso deste script
Para usar esse script python você precisa clonar o repositório: 
```bash
git clone https://github.com/GabrielTheophilo/NewsApiScript.git
```

Abra a pasta que você clonou

Registre uma chave para a API no site [NewsApi](https://newsapi.org/)

Abra o arquivo apikey.py e adicione a chave de 32 caracteres após o 'apikey=', exemplo: 'apikey=SUACHAVEAQUI'

Rode o newsscript.py e siga os comandos do terminal

IMPORTANTE: Se você tem o plano gratuito da API, sua pesquisa estará limitada a uma página, então quando o programa pedir o número de páginas da sua busca, por favor especifique como "1", ou a API retornará um erro após imprimir a primeira página, com o código "maximumResultsReached".

Depois de rodar o código, um arquivo .json será criado com as informações e links sobre o tópico que você pesquisou. Abra com qualquer editor de texto ou IDE de sua preferência para acessar o arquivo .json.


