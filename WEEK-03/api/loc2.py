import requests,json

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=14.4669&longitude=75.9269&hourly=dew_point_2m,rain,wind_speed_10m")
data = response.json()
print(json.dumps(data,indent=4))
with open ("02.json" ,'w')as f:
    f.write(json.dumps(data,indent=4))