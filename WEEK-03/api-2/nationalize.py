# import requests,json

# url = "https://api.nationalize.io/?name=Siddesh"

# response = requests.get(url)
# data = response.json()
# print(json.dumps(data,indent=4))

import requests
import json
import time

MAX_REQUESTS = 100
request_count = 0

def call_api(name):
    global request_count

    if request_count >= MAX_REQUESTS:
        print("409: Rate limit exceeded (more than 100 requests)")
        return None  # or raise exception

    url = f"https://api.nationalize.io/?name=Siddesh"
    response = requests.get(url)

    request_count += 1  # count every GET call

    return response.json()

for i in range(110):
    print(f"Request #{i+1}")

    result = call_api("Siddesh")

    if result is None:
        break   # stop further requests

    print(json.dumps(result, indent=4))
    time.sleep(0.1)  # optional delay so it doesn't spam
