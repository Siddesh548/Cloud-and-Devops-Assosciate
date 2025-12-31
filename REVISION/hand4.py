# import requests
# import json

# url = "https://dummyjson.com/products/2"

# r = requests.get(url)
# data = r.json()
# # print(data)
# # for product in data["products"]:
# for review in data.get("reviews", []):
#     if review["rating"] == 5:
#         review["rating"] = 4

# patch_data = {"reviews": data["reviews"]}

# try:
#     patch_resp = requests.patch(url, json=patch_data, timeout=10)
#     patch_resp.raise_for_status()
#     updated_data = patch_resp.json()

#     with open("uhand4.json", "w") as f:
#         json.dump(updated_data, f, indent=4)

#     print("PATCH update saved to API and local file.")
#     print("Response Code:", patch_resp.status_code)

# except requests.Timeout:
#     print("Request timed out")
# except requests.ConnectionError:
#     print("Connection failed")
# except requests.HTTPError as e:
#     print("HTTP error:", e)
# except requests.RequestException as e:
#     print("Error occurred:", e)
