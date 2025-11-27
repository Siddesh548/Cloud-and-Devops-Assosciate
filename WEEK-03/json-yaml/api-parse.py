import requests, json,yaml

r = requests.get("https://jsonplaceholder.typicode.com/posts")

##########JSON --> Python DICT##########

response = r.json()
#print(json.dumps(response,indent=4)   ##Python dict --> JSON (json.dumps)
       #or#
# print(json.dumps(r.json(), indent=2))
# with open("js-py.json","w") as f:
#     f.write(json.dumps(r.json(),indent=5))

##########JSON --> YAML##########

#yaml_data = yaml.dump(response) 
# print(yaml_data)
     ##or##
print(yaml.dump(response)) ##JSON-->YAML(yaml.dump)
with open("yml_jsn.yaml","w") as f:
    f.write(yaml.dump(response))

##############YAMl --> JSON############
# js_py = yaml.safe_load(yaml_data) ##YAML(yaml.safe_load)--> PYTHON DICT (json.dumps)--> JSON
# print(json.dumps(js_py,indent=4))

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
# response
# data = yaml.safe_load(response)
# print(data)


# #yaml_data = yaml.safe_load(response.text)

# json_data = json.dumps(response, indent=4)

# #data = response.json()
# print(json_data)


# url = "https://jsonplaceholder.typicode.com/posts/1"

# # 1. Fetch JSON from API
# response = requests.get(url)

# if response.status_code != 200:
#     print("Error fetching API:", response.status_code)
#     exit()

# json_data = response.json()
# print(json_data)       # JSON → Python dict

# print("Fetched JSON:")
#print(json.dumps(json_data, indent=4))

# # 2. Convert JSON → YAML
# yaml_data = yaml.dump(json_data, sort_keys=False)

# print("\nConverted to YAML:")
# print(yaml_data)

# # 3. Convert YAML → Python dict
# yaml_dict = yaml.safe_load(yaml_data)

# # 4. Convert back to JSON
# json_again = json.dumps(yaml_dict, indent=4)

# print("\nConverted YAML → JSON:")
# print(json_again)

# # 5. Save to files
# with open("post_1.json", "w") as f_json:
#     f_json.write(json.dumps(json_data, indent=4))

# with open("post_1.yaml", "w") as f_yaml:
#     f_yaml.write(yaml_data)

# print("\n✔ Saved post_1.json and post_1.yaml")
