import requests
from django.shortcuts import render

# Create your views here.


def cnn(request):
    """Connect to CNN search API, do the search then return the result."""
    url = ('https://search.api.cnn.io/content?'
           'q=covid+coronavirus&size=25&from=0&type=article')
    json_data = requests.get(url).json()
    data = json_data['result']
    return render(request, 'covidnews/cnn.html', {'data': data})
