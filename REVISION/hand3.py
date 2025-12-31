import requests
import json

# url = "https://dummyjson.com/products"

# r = requests.get(url)
# data = r.json()

# with open("hand22.json","w") as f:
#     data = json.dump(data,f,indent=4)
# # print(data)

# with open ("hand22.json","r") as f:
#     data = json.load(f)

# new_review = {
#     "id": 35,
#     # max([rev["id"] for rev in data.get("reviews", [])]+[0]) + 1,
#     "rating": 5,
#     "comment": "Amazing product!",
#     "date": "2025-12-19T12:00:00.000Z",
#     "reviewerName": "New User",
#     "reviewerEmail": "new.user@example.com"
# }

# if "reviews" not in data:
#     data["reviews"] = []
# data["reviews"].append(new_review)

# with open("uhand2.json","w") as f:
#     json.dump(data ,f ,indent=4)

# print("update saved")


#To check the data is added or not
# with open("uhand2.json", "r") as f:
#     data = json.load(f)

# new_review_id = 35  
# for review in data["reviews"]:
#     if review["id"] == new_review_id:
#         print("Found review:", review)

# To delete the data 
# with open("uhand2.json", "r") as f:
#     data = json.load(f)

# new_review_id = [] 

# for review in data["reviews"]:
#     if review["id"] != 35:
#         new_review_id.append(review)

# data["reviews"] = new_review_id

# with open("uhand2.json","w") as f:
#     json.dump(data,f,indent=4)

#To check data is deleted or not
with open("uhand2.json", "r") as f:
    data = json.load(f)

found = False 
for review in data["reviews"]:
    if review["id"] == 35:
        found = True
        break
if not found:
    print("deleted")
else:
    print("still exists")
    