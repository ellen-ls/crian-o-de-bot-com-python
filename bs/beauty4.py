import bs4
import requests

def extrair_frases():
    r = requests.get('https://quotes.toscrape.com/')
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    frases = soup.findAll('span', {'class':'text'})
    frases_sem_tag = []
    for frase in frases:
        frases_sem_tag.append(frase.string)
    

    return frases_sem_tag

def extrair_primeira_frase():
    primeira_frase = extrair_frases()
    
    return primeira_frase[0]
    
    
    
def extrair_autores():
    r = requests.get('https://quotes.toscrape.com/') 
    html = r.text                                     
    soup = bs4.BeautifulSoup(html, 'html.parser')     
    autores = soup.findAll('small')
    autores_sem_tag = []
    
    for autor in autores:
        autores_sem_tag.append(autor.string)
    
    return(autores_sem_tag)



def extrair_primeiro_autor():
    primeiro_autor = extrair_autores()
    
    return primeiro_autor[0]

print(extrair_primeiro_autor())
    


