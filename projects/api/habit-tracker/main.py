import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": " Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now().strftime("%Y%m%d")
print(today)
pixel_config = {
    "date": today,
    "quantity": "122.4",
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_config, headers=headers)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{today}"

pixel_update_config = {
    "quantity": "54.3"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_config, headers=headers)
# print(response)

DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{today}"

# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)
