import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://images.pexels.com/photos/1181403/pexels-photo-1181403.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2FhYzE1YWM3OGU2ZDhiOTpiMTE4NzJlZjAxZTM4ODhkZDZhZGUxMzYzOTFhM2IxNg=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(10):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
