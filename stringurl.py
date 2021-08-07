from apikey import ApiKey

class StringUrl(ApiKey):
    key = ApiKey.key
    urlTop = 'https://newsapi.org/v2/top-headlines?'
    urlAll = 'https://newsapi.org/v2/everything?'
    pagesize = 'pageSize=100&'
    country = 'country=br&'
    language =  'language=pt&'
    popularity = 'sortBy=relevancy&'
    relevancy = 'sortBy=popularity&'
    url = ''
    query = ''
    def __init__(StringAll, StringSort,LanguageQuery, Query):
        if StringAll == '1' or StringAll == '':
            StringUrl.url += StringUrl.urlAll
        else:
            StringUrl.url += StringUrl.urlTop
            
        if StringSort == '1' or StringSort == '':
            StringUrl.url += StringUrl.relevancy
        elif StringSort == '2':
            StringUrl.url += StringUrl.popularity

        if LanguageQuery == '1':
            StringUrl.url += StringUrl.language
        StringUrl.url += (f'q={Query}&')
        StringUrl.url += StringUrl.pagesize
        StringUrl.url += StringUrl.key
        StringUrl.query += Query
        
        return StringUrl.url

    def StringAll():
        return str(input('Deseja ver todas as notícias ou apenas as Top-Headlines? || 1 para Todas, 2 para Principais: '))
    
    def StringSort():
        return str(input('Deseja ordernar sua busca? || Digite 1 para Relevância, 2 para Popularidade, 3 para não ordernar: '))

    def Query():
        return str(input("Selecione o termo que deseja pesquisar: "))
    
    def LanguageQuery():
        return str(input("Deseja receber notícias apenas em português ou todas? || 1 para Português, 2 para Todas: "))
    def ApiKey():
        return str(ApiKey.key)
        