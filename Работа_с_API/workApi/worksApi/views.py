from django.shortcuts import render
from django.http import HttpResponse
import requests


def WorkAPI(request):
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    data = response.json()
    print('Данные в консоли', data)
    return render(request, 'data.html', {'data': data})

def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def lists(request):
    return render(request, 'list.html')

def card(request):
    return render(request, 'card.html')


