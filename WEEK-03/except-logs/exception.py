import subprocess

ips = ["192.168.1.1", "8.8.8.8", "1.1.1.1"]

for ip in ips:
    print(f"Pinging {ip} ...")
    try:
        result = subprocess.run(
            ["ping", "-n", "1", ip],    
            timeout=0.5                   
        )
        if result.returncode == 0:
            print(f"{ip} is reachable\n")
        else:
            print(f"{ip} is NOT reachable\n")

    except subprocess.TimeoutExpired:
        print(f"{ip} ping timed out\n")


