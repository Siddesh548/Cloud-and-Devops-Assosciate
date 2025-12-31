# import requests
# import json

# APIkey = "42c479f3e789ede5b767704afa6db564"

# url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={APIkey}"

# response = requests.get(url)

# print(response.status_code)
# print(json.dumps(response.json(),indent=2))



# import requests

# APIkey = "42c479f3e789ede5b767704afa6db564"

# url = "https://api.openweathermap.org/data/2.5/weather"

# params = {
#     "lat": 44.34,
#     "lon": 10.99,
#     "appid": APIkey
# }

# response = requests.get(url, params=params)

# print(response.status_code)
# print(response.json())
