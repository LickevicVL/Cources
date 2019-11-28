from pprint import pprint

import requests

if __name__ == '__main__':
    response = requests.get(
        'https://api.github.com/user/repos',
        headers={'Authorization': f'token {input("token: ")}'}
    )
    print(response.status_code)
    pprint(response.json())
