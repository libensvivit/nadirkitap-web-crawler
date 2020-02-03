import requests, json
from bs4 import BeautifulSoup

def getBooks(pages=1):
    books_list = []

    for page in range(pages):
        url = 'https://www.nadirkitap.com/kitapara.php?listele=ensoneklenenler&page=' + str(page+1)
        books_dict = {}

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        for ul in soup.find_all('ul', {'class': 'product-list'}):
            for li in ul.find_all('li'):
                div = li.find('div', {'class': 'col-md-8'})
                
                if div:
                    books_dict = {}
                    title_text = div.h4.a.select_one('span').text
                    author_text = div.p.text
                    date_text = div.ul.find_all('li')[1].select_one('span').text[-4:]
                    cost_text = li.find('div', {'class': 'col-md-6 col-xs-12 no-padding text-right product-list-price'}).text

                    #title = title_text if len(title_text) < 50 else title_text[:50]
                    #author = author_text if len(author_text) < 30 else author_text[:30]
                    date = date_text if date_text.isdigit() else ""
                    cost = cost_text[:-3]

                    books_dict['title'] = title_text
                    books_dict['author'] = author_text
                    books_dict['cost'] = cost
                    books_dict['published'] = date
                    books_dict['href'] = div.h4.a.get('href')

                    books_list.append(books_dict)

    #exportBooks(books_list)
    return books_list

def exportBooks(books_list):
    with open('data.json', 'w', encoding='utf8') as outfile:
         json.dump(books_list, outfile, indent=2, ensure_ascii=False)