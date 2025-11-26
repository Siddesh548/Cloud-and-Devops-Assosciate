import yaml
import json
# with open("sim.yaml") as f:
#      data = yaml.safe_load(f)
#     #read = f.read()
# print(data) 

#########################

# with open("docker-yaml.yaml") as f:
#     data = yaml.safe_load(f)
#     # for i in data:
#     #     print(data[i].keys())
# print(data["services"]["mysql"]["environment"])

############################################

# with open("docker-yaml.yaml") as f:
#     data = yaml.safe_load(f)
# lst = data["services"]["oai-udm"]
# #print(lst)
# envv = lst.get("environment", [])
# dict={}
# for i in envv:
#     if "=" in i:
#         key,value=i.split("=",1)
#         dict[key]=value
# print(dict.get("TZ"))
# json_data = json.dumps(data,indent=2)

# with open("docker-yaml.yaml") as f:
#     data = yaml.safe_load(f)
# datas = data["services"]["mysql"]["environment"]
# # envv = datas.get("environment", [])
# env_dict = {}
# for i in datas:
#     if "=" in i:
#         key,value = i.split("=",1)
#         env_dict[key] = value
# print(env_dict)



#############################################

