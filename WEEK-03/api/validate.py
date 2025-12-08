import requests,json


# response = requests.get(url)
# data = response.json()
# print(json.dumps(data,indent=4))

def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url) 
        response.raise_for_status() 

    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

url = "http://api.ipapi.com/api/161.185.160.93?access_key=2f38de56e34f383bd77224db589e72c"  #2f38de56e34f383bd77224db589e72ac
print(fetch_data(url))

# good_url = "https://api.restful-api.dev/objects"
# print(fetch_data(good_url))

# bad_url = "https://jsonplaceholder.typicode.com/todos_wrong"
# print(fetch_data(bad_url))

# bad_json_url = "https://example.com"
# print(fetch_data(bad_json_url))

