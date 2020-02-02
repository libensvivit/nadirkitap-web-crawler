import requests, json
from bs4 import BeautifulSoup

def getBooks():
    url = 'https://www.nadirkitap.com/yeni-eklenen-kitaplar.html'
    books_list = []
    books_dict = {}

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    for ul in soup.find_all('ul', {'class': 'product-list'}):
        for li in ul.find_all('li'):
            div = li.find('div', {'class': 'col-md-8'})
            if div:
                books_dict = {}
                title_text = div.h4.a.select_one('span').text
                title = title_text if len(title_text) < 50 else title_text[:50]
                date = div.ul.find_all('li')[1].select_one('span').text[-4:]

                books_dict['title'] = title
                books_dict['author'] = div.p.text
                books_dict['href'] = div.h4.a.get('href')
                books_dict['published'] = date if date.isdigit() else ""

                books_list.append(books_dict)


    with open('data.json', 'w', encoding='utf8') as outfile:
        json.dump(books_list, outfile, indent=2, ensure_ascii=False)
    return books_list