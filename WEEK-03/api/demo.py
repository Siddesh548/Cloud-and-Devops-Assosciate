import requests ,json

############ GET ###############

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
# print(data) #--->python objects
#print(json.dumps(data,indent=4))  #python objects -->json



######### POST ##########

url = ("https://jsonplaceholder.typicode.com/posts")
datas = {'userId':11,'id':95,'title':'python'}
response = requests.post(url,json=datas)
data = response.json()
print(json.dumps(data,indent=4))
print('status',response.status_code)
