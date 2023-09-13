import requests
from bs4 import BeautifulSoup

url = 'https://stepik.org/'
response = requests.get(url) #GET-запрос на сайт 

soup = BeautifulSoup(response.text, 'html.parser') #передаём содержимое ответа в объект BeautifulSoup 

articles = []                                 #чтобы найти заголовки и описания статей на странице,
for article in soup.find_all('article'):      #найдем все теги заголовков (обычно они имеют тег h2 или h3)
    title = article.find('h2').text           #и их следующий за ним элемент (часто это тег p)
    description = article.find('p').text
    articles.append({
        'title': title,
        'description': description
    })
    
print(articles) #в результате получим список словарей, каждый из которых содержит заголовок и описание статьи
