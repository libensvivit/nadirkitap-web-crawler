#import telegram
from django.shortcuts import render
from .nadir import getBooks

#bot = telegram.Bot(token='<YOUR-TOKEN>')
#chat_id = bot.get_updates()[-1].message.chat_id
book_list = []


def informMe(of_new_books):
    if of_new_books:
        if len(of_new_books) < 5:
            for book in of_new_books:
                bot.send_message(chat_id=chat_id, text=book)


def updatedBookList(books, data):
    new_books = []
    for item in data:
        if item['title'] not in books:
            new_books.append(item['title'])
            book_list.append(item['title'])
            data[data.index(item)]['title'] = '[NEW] ' + item['title']
    return new_books


def send_json(request):
    new_data = getBooks()
    #new_books = updatedBookList(book_list, new_data)
    #informMe(new_books)

    return render(request, 'page.html', {'data': new_data})
