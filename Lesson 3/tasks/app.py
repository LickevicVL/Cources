from os import environ, path

import requests
from flask import Flask
from flask import Response
from json import dumps

SITES = [
    'https://google.com',
    'https://ya.kotletka.net',
    'https://python.org',
    'https://test.test'
]

app = Flask(__name__)


@app.route('/')
def check():
    sites = SITES.copy()

    file = environ.get('FILE')
    if file and path.isfile(file):
        with open(file) as fl:
            sites = fl.read().split('\n')

    results = []
    for site in sites:
        try:
            requests.get(site)
            if requests:
                results.append(f'Site: {site} is available')
            else:
                results.append(f'Site: {site} is not available')
        except requests.ConnectionError:
            results.append(f'Site: {site} is not exit')

    return Response(
        response=dumps(results),
        headers={'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
