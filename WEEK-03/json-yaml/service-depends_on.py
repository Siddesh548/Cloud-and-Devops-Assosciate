# import yaml

# with open("docker-yaml.yaml") as f:
#     data = yaml.safe_load(f)

# services = data.get("services", {})

# for service_name, service_data in services.items():
#     print("Service:", service_name)

#     depends = service_data.get("depends_on",[])
#     print(f"depends_on:",depends if depends else "None")


###########################################3

import yaml

with open("docker-yaml.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

for service_name, service_data in services.items():
    print("Service:", service_name)
    depends = service_data.get("depends_on",[])
    print(f"depends_on:",depends if depends else "None")

for service_name, service_data in services.items():
    print("Service:", service_name)
    networks = service_data.get("networks", {})
    print(networks)

for service_name, service_data in services.items():
    print("Service:", service_name)
    env_list = service_data.get("environment",[])
    env_ports = []
    for item in env_list:
        if "=" in item:
            key,value = item.split("=",1)
            if "_PORT" in item:
                env_ports.append(f"{key}={value}")
    env_ports_unique = list(set(env_ports)) #list(dict.fromkeys(env_ports))
    print(env_ports_unique)
    #print(env_port)
  
    