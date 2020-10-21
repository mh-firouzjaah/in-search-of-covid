from datetime import date

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'


@app.route('/cnn-covid')
def cnn():
    """Connect to CNN search API, do the search then return the result."""
    url = ('https://search.api.cnn.io/content?'
           'q=covid+coronavirus&size=25&from=0&type=article')
    json_data = requests.get(url).json()
    data = json_data['result']
    return render_template('flask/cnn.html', data=data)


@ app.route('/worldometers')
def worldometers():
    """Connect to worldometers and get the latest news"""
    url = 'https://www.worldometers.info/coronavirus/'
    url_contents = requests.get(url).content
    soup = BeautifulSoup(url_contents, "html.parser")
    today = date.today()
    div = soup.find("div", {'id': f'newsdate{today}'})
    for a in div.find_all('a'):
        if not 'http' in a['href']:
            a['href'] = 'https://www.worldometers.info/' + a['href']
    return render_template('flask/worldometers.html', data=div)


if __name__ == "__main__":
    app.run(debug=True)
