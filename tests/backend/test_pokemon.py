import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = 'e0c88f67f587becb93e7c7300c8b6b5d'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 2203})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 2203})
    assert response.json()['data'][0]['trainer_name'] == 'Софья'
