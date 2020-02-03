from django.shortcuts import render
from django.http import HttpResponse
from .nadir import getBooks
import json

def index(request):
    return render(request, 'index.html')

def serve_data(request):
        data = getBooks()
        return HttpResponse(json.dumps(data), content_type="application/json")
