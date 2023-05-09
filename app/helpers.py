import requests, json

def getName(i):
    url= f'https://www.dnd5eapi.co/api/monsters'
    response = requests.get(url)
    if response.ok:
        api = response.json()
        monster_info = {}
        monster_info['name'] = api['results'][i]['index']
        return monster_info['name']
    
def test():
        name = 'bat'
        url = f'https://www.dnd5eapi.co/api/monsters/{name}'
        response = requests.get(url)
        if response.ok:
            print(response.ok)
            api = response.json()
            print(api['senses'])
