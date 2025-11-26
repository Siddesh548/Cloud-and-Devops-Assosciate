import json
with open("wireshark.json") as f:
    data = json.load(f)
    print(data["_index"])
#     for item in data:
#         print(item["_source"]["layers"])
# print(data["_source"]["layers"])

############################

# import json

# with open("wireshark.json") as f:
#     data = json.load(f)
#     first = data[0]
#     for item in first:
        
#         layers = item["_source"]["layers"][0]

#         if "ipv6" in layers:
#             print("IPv6 layer:", layers["ipv6"])

#         elif "ip" in layers:
#             print("IPv4 layer:", layers["ip"])

#         else:
#             print("No IP layer found in this packet")
