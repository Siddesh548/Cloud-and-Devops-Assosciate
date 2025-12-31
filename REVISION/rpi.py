# import requests
# import json

# BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# # # ---------- CREATE ----------
# # def create_post():
# #     payload = {
# #         "title": "API Learning",
# #         "body": "Learning CRUD with Python",
# #         "userId": 1
# #     }
# #     r = requests.post(BASE_URL, json=payload)
# #     print("CREATE:", r.status_code)
# #     print(json.dumps(r.json(), indent=2))


# # ---------- READ ----------
# # def read_post(post_id):
# r = requests.get(f"{BASE_URL}")
# print("READ:", r.status_code)
# print(json.dumps(r.json(), indent=2))


# # # ---------- UPDATE (PUT) ----------
# # def update_post(post_id):
# #     payload = {
# #         "id": post_id,
# #         "title": "Updated Title",
# #         "body": "Updated content",
# #         "userId": 1
# #     }
# #     r = requests.put(f"{BASE_URL}/{post_id}", json=payload)
# #     print("UPDATE:", r.status_code)
# #     print(json.dumps(r.json(), indent=2))


# # # ---------- DELETE ----------
# # def delete_post(post_id):
# #     r = requests.delete(f"{BASE_URL}/{post_id}")
# #     print("DELETE:", r.status_code)
# #     print("Post deleted")


# # # ---------- MAIN ----------
# # create_post()
# # read_post(1)
# # update_post(1)
# # delete_post(1)
