# import requests
# import json

# url = "https://dummyjson.com/products"

# r = requests.get(url)
# data = r.json()
# with open("hand2.json","w") as f:
#     data = json.dump(data,f,indent=4)
# # print(data)

# with open ("hand2.json","r") as f:
#     data = json.load(f)

# reviews = []
# for product in data["products"]:
#     for review in product["reviews"]:
#         if product["id"] == 2 and review["rating"] == 5:
#             review["rating"] = 4
#             reviews.append({review["reviewerName"],product["id"],review["rating"]})
# print(reviews)

# with open("uhand.json","w") as f:
#     json.dump(data ,f ,indent=4)

# print("update saved")