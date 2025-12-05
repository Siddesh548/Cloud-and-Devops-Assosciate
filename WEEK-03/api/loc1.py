import requests,json

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=12.8949&longitude=77.6261&hourly=dew_point_2m,rain")
data = response.json()
print(json.dumps(data,indent=4))
with open ("01.json" ,'w')as f:
    f.write(json.dumps(data,indent=4))
    