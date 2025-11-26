import yaml

with open("docker-yaml.yaml") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})

for service_name, service_value in services.items():
    print("Service:", service_name)
    
    # Extract IPv4 address if defined
    networks = service_value.get("networks", {})
    print(networks)
    # ip_addresses = []
    # for net_name, net_data in networks.items():
    #     ip = net_data.get("ipv4_address")
    #     if ip:
    #         ip_addresses.append(ip)
    
    # print("IP Address(es):", ip_addresses if ip_addresses else "No IP defined")
    # print("-" * 40)
