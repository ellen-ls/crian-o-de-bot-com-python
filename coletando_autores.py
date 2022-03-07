import requests

def coletando_autores():    
    r = requests.get('https://quotes.toscrape.com/')
    # print(r.text)

    html = r.text.split('\n')
    # print(html)

    autores = []

    for linha in html:
        if '<small class="author" itemprop="author">' in linha:
            linha_editada = linha.replace('<span>by <small class="author" itemprop="author">', '')
            linha_editada = linha_editada.replace('</small>', '')
            linha_editada = linha_editada.strip()
            autores.append(linha_editada)
    
    return autores
        

def coletando_primeiro_autores():
    autores = coletando_autores()
    print (autores)

coletando_primeiro_autores()