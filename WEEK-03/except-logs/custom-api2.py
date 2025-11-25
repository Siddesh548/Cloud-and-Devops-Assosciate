# import requests  

# def custom_api_response(status, message, data=None, error=None):
#     return {
#         "status": status,
#         "message": message,
#         "data": data,
#         "error": str(error) if error else None
#     }

# def fetch_data_from_api(url):
#     try:
#         print(f"\nFetching: {url}")
#         response = requests.get(url, timeout=3)
#         response.raise_for_status() 

#         # success
#         return custom_api_response(
#             status="success",
#             message="Data fetched successfully",
#             data=response.json()
#         )

#     except requests.exceptions.Timeout as e:
#         return custom_api_response(
#             status="timeout_error",
#             message="The request timed out",
#             error=e
#         )

#     except requests.exceptions.HTTPError as e:
#         return custom_api_response(
#             status="http_error",
#             message="HTTP error occurred",
#             error=e
#         )

#     except requests.exceptions.ConnectionError as e:
#         return custom_api_response(
#             status="connection_error",
#             message="Failed to connect to the server",
#             error=e
#         )

#     except Exception as e:
#         return custom_api_response(
#             status="unexpected_error",
#             message="An unexpected error occurred",
#             error=e
#         )


# # ----------------- TESTING -----------------

# good_url = "https://jsonplaceholder.typicode.com/posts/1"
# bad_url = "https://wrong-domain-example-12345.com/api"

# print("\nTesting GOOD URL:")
# print(fetch_data_from_api(good_url))

# print("\nTesting BAD URL:")
# print(fetch_data_from_api(bad_url))


###################################################################

import requests

class InvalidAPIResponse(Exception):
    pass

def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError:
            raise InvalidAPIResponse("Response is not valid JSON")

        print("Data fetched successfully!")
        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except InvalidAPIResponse as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

good_url = "https://api.restful-api.dev/objects"
print(fetch_data(good_url))

bad_url = "https://jsonplaceholder.typicode.com/todos_wrong"
print(fetch_data(bad_url))

bad_json_url = "https://example.com"
print(fetch_data(bad_json_url)) 