import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
try:

    r = requests.get(url,timeout=10)
    r.raise_for_status()
    data = r.json()

    with open("hand.json","w") as f:
        json_data = json.dump(data,f,indent=4)
        #print(json_data)

    
        payload = {
        "userId":11,
        # "id":11,
        "title":"something new",
        "body":"making HTTP requests. The PUT method is one of the key HTTP request methods used to update or create a resource at a specific URI"
    }
        
    resp = requests.post(url,json=payload,timeout=10)
    print(resp.status_code)
    with open("hand.json","w")as f:
        updated_json=json.dump(resp.json(),f,indent=2)

except requests.Timeout as time:
    print("requested timed out")

except requests.ConnectionError :
    print("connectionn failed")

except requests.HTTPError as http_error:
    print(resp.status_code)

except requests.RequestException as e:
    print("error occured")