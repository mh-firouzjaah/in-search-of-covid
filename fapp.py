import requests
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
    return render_template('cnn.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
