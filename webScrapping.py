from bs4 import BeautifulSoup
import requests
import re
import urllib.parse
import pandas

dict_produtos_existentes = {"titulo": []}

df = pandas.read_csv('produtos.csv')

siteUrl = "https://revendas.cedet.com.br/index.php?route=product/search&search="

dict_produtos = {'produtos': []}

for j in range(len(df)):
    
    item = df["Produtos"][j]
    
    safe_string = urllib.parse.quote_plus(item)
 
    url = siteUrl + safe_string

    print(f'Iniciando a extração do site https://revendas.cedet.com.br, item: {item}')

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition std-1)'}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    
    produtos = soup.find_all('div', class_=re.compile('item-product'))
    
    produto = produtos[0]
    
    itemUrl = produto.find('a',class_=re.compile('link-card btn-ripple')).get("href")
    
    itemPage = requests.get(itemUrl, headers=headers)
    soup = BeautifulSoup(itemPage.content, 'html.parser')
    
    notifyMe = soup.find_all('a', class_=re.compile('button nwa_list_button_custom'))
    
    if notifyMe:
        dict_produtos_existentes['titulo'].append(item)

   
    
