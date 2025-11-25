import subprocess

def check_ip_reachability():
    ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

    for ip in ips:
        re = subprocess.run(f"ping -n 1 {ip}")

        if re.returncode == 0:
            print(f"IP address {ip} is reachable")
        else:
            print(f"IP address {ip} is not reachable")

check_ip_reachability()



#########

# import os

# ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

# for ip in ips:
#     print(f"Pinging {ip} ...")
#     response = os.system(f"ping -n 1 {ip} >nul")   # use -c 1 for Linux

#     if response == 0:
#         print(f"{ip} is reachable\n")
#     else:
#         print(f"{ip} is NOT reachable\n")

