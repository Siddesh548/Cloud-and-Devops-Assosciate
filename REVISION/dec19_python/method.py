import requests
import json

headers = {
    "Authorization":f"Beaer reqres-token ",
    "Accept":"application/json"
}
url = "https://reqres.in/api/users/2"

re = requests.get(url)
data = re.json()

print(json.dump(data,indent=2))

payload = {
    "job":"architect"
}

response = requests.put(url,json=payload)
response.raise_for_status()
data = response.json()
print(data)