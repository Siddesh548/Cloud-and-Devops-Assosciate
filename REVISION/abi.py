# import requests

# def validate_username():
#     api_url = "https://reqres.in/api/users"
    
#     headers = {
#         "Authorization": "Bearer reqres-token",
#         "Content-Type": "application/json"
#     }
    
#     payload = {
#         "name": "smith",
#         "job": "agent"
#     }
    
#     response = requests.post(api_url, json=payload, headers=headers)
    
#     if response.status_code != 201:
#         return False
    
#     response_data = response.json()
    
#     # Data analysis: verify name matches input
#     if response_data.get("name") == payload["name"]:
#         return True
#     else:
#         return False


# # Run validation
# result = validate_username()
# print(result)
