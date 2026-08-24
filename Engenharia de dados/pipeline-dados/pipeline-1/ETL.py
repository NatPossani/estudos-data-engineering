#biblioteca que permite requisições HTTP para sites e APIs
import requests
#import pandas as pd
import json

#ETL - Extract, Transform, Load
#funcao extrair
def extract_data(endpoint):
    response= requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"erro ao extrair dados da APOI: {response.status_code}")
        return None

#funcao load
def load_data(data, path):
    id = data["id"]
    #dentro da pasta path, criar um arquivo json com o nome do arquivo sendo o id o nome do endpoint
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)

def loop_load_data(endpoint):
    endpoint = "https://dummyjson.com/" + endpoint
    i = 1
    while True:
        data = extract_data(endpoint + str(i))
        if data:
            load_data(data, endpoint)
        else:
            print(f"erro ao extrair pdados da API: {data}")
            break
        i += 1

endpoints = ["users", "products"]

for endpoint in endpoints:
    loop_load_data(endpoint)