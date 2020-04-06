import requests
import json






def send_data(data):
    url = "http://127.0.0.1:8080/SendData"
    #print(json.dumps(data))
    payload = json.dumps(data)
    headers = {
      'Content-Type': 'application/json',
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))



def index():
    url = "http://127.0.0.1:8080/"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()



#index()

data = {
    "type":"jaraem_takhir_dar_bahre_bardari",
    "id_ghest":"1",
    "id_gostare":"1"
}


send_data(data)
