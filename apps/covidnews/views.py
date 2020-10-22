from datetime import date

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.


def cnn(request):
    """Connect to CNN search API, do the search then return the result."""
    url = ('https://search.api.cnn.io/content?'
           'q=covid+coronavirus&size=25&from=0&type=article')
    json_data = requests.get(url).json()
    data = json_data['result']
    return render(request, 'covidnews/cnn.html', {'data': data})


def worldometers(request):
    """Connect to worldometers and get the latest news"""
    url = 'https://www.worldometers.info/coronavirus/'
    url_contents = requests.get(url).content
    soup = BeautifulSoup(url_contents, "html")
    today = date.today()
    div = soup.find("div", {'id': f'newsdate{today}'})
    for a in div.find_all('a'):
        if not 'http' in a['href']:
            a['href'] = 'https://www.worldometers.info/' + a['href']
    return render(request, 'covidnews/worldometers.html', {'data': div})
