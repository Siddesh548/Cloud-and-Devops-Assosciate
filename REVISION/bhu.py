# import requests
# import time
# import socket

# URLS = [
#     "http://httpbin.org/get",
#     "http://httpbin.org/headers",
#     "http://httpbin.org/ip",
#     "http://httpbin.org/user-agent"
# ]

# def get_server_ip(host):
#     return socket.gethostbyname(host)

# def measure_rtt(url):
#     start = time.time()
#     response = requests.get(url)
#     end = time.time()
#     return (end - start) * 1000, response

# def main():
#     host = "httpbin.org"
#     server_ip = get_server_ip(host)
#     print(f"Server IP: {server_ip}\n")

#     results = []

#     for i, url in enumerate(URLS):
#         rtt, response = measure_rtt(url)
#         results.append((i, url, rtt))
#         print(f"TCP Stream {i}")
#         print(f"Target: {url}")
#         print(f"Status Code: {response.status_code}")
#         print(f"Approx RTT: {rtt:.2f} ms\n")

#     print("Average RTT comparison:")
#     for stream, url, rtt in results:
#         print(f"Stream {stream}: {rtt:.2f} ms")

#     print("\nDHCP Info:")
#     print("Not available via HTTP request (requires packet capture during IP assignment)")

# if __name__ == "__main__":
#     main()
