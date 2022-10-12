import requests, os

HEADERS = {
    'X-Auth-Token': os.getenv('API_KEY')
}

def handle_request(url: str):
    response = requests.get(url, headers=HEADERS)
    return response.json()
