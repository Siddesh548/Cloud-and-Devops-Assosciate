# import requests,json

# BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# # ---------------- CREATE ----------------
# create_data = {
#     "title": "Hello",
#     "body": "Learning CRUD",
#     "userId": 1,
#     "id":1
# }

# create_res = requests.post(BASE_URL, json=create_data)
# print("\nCREATE (POST)")
# print(create_res.json())


# # ---------------- READ ----------------
# read_res = requests.get(f"{BASE_URL}/1")
# print("\nREAD (GET)")
# print(read_res.json())
# with open("filenane.json","w") as f:
#     json.dump(read_res.json,f,indent=2)


# # ---------------- UPDATE (PUT - full update) ----------------
# update_data = {
#     "title": "Hello - Updated",
#     "body": "Learning CRUD - Updated using PUT",
#     "userId": 1
# }

# update_res = requests.put(f"{BASE_URL}/1", json=update_data)
# print("\nUPDATE (PUT)")
# print(update_res.json())


# # ---------------- PATCH (partial update) ----------------
# patch_data = {
#     "title": "Hello - Patched"
# }

# patch_res = requests.patch(f"{BASE_URL}/1", json=patch_data)
# print("\nPATCH (Partial Update)")
# print(patch_res.json())


# # ---------------- DELETE ----------------
# delete_res = requests.delete(f"{BASE_URL}/1")
# print("\nDELETE")
# print("Status Code:", delete_res.status_code)
