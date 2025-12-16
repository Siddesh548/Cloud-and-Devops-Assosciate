import requests
import logging
import json


# r = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(r.status_code)

# try:
#     r = requests.get("https://jsonplacehhholder.typicode.com/posets")
# #     r.raise_for_status()
# # except requests.exceptions.HTTPError as err:
# #     print('bad request', r.status_code)

# except requests.exceptions.RequestException as err:
#     print('connection failed')

logging.basicConfig(
    filename= "rev-api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("gettting info from url")
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    r.raise_for_status()

    data = r.json()
    # print(data)

    with open("rev-api.json",'w') as f:
        json.dump(data,f,indent=2)
    
    count = {}

    for id in data:
        # print(id["userId"])
        uid = id["userId"]
        
        if uid in count:
            count[uid] += 1
        
        else:
            count[uid] = 1
    
    for uid in count:
        print(count[uid])

except requests.exceptions.HTTPError as err:
    print('bad request', r.status_code)
    logging.error("page not founnd")

except requests.exceptions.RequestException as err:
    print('connection failed')
    logging.error("connection unsuccessfull")