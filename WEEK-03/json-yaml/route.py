import json
import subprocess

def get_route_table():
    # Run "ip route" command
    result = subprocess.run(["ip", "route"], capture_output=True, text=True)
    output = result.stdout.strip().split("\n")

    routes = []

    for line in output:
        parts = line.split()
        route = {}

        # Destination (always first)
        route["route"] = parts[0]

        i = 1
        while i < len(parts):
            token = parts[i]

            if token == "via":
                route["via"] = parts[i + 1]
                i += 2

            elif token == "dev":
                route["interface"] = parts[i + 1]
                i += 2

            elif token == "proto":
                route["protocol"] = parts[i + 1]
                i += 2

            elif token == "src":
                route["source"] = parts[i + 1]
                i += 2

            elif token == "metric":
                route["metric"] = parts[i + 1]
                i += 2

            else:
                # flags like "linkdown", "scope", etc.
                route.setdefault("flags", []).append(parts[i])
                i += 1

        routes.append(route)

    return routes


# Convert to JSON and save to file
route_table = get_route_table()
json_output = json.dumps(route_table, indent=4)

print(json_output)

with open("route_table.json", "w") as f:
    f.write(json_output)

print("\nSaved as route_table.json")
