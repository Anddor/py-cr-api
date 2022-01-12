import requests
import json
import os

player_tags = [''] # ADD PLAYER TAGS HERE
keep_fields = ["name", "wins"]
BASE_URL = 'https://api.clashroyale.com/v1/players/%23'

token = os.environ["CLASHR_TOKEN"] # ADD TOKEN HERE

headers = {
    "authorization" : "Bearer " + token,
    "accept": "application/json"
}

def get_player_data(player_tags, keep_fields):
    result_list = []
    for tag in player_tags:
        player_url = BASE_URL + tag
        response = requests.get(player_url, data = {}, headers=headers)
        response_json = json.loads(response.text)
        player_dict = {k:response_json.get(k,None) for k in keep_fields }
        result_list.append(player_dict)
    return result_list

print(get_player_data(player_tags, keep_fields))