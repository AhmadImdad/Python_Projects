import requests
import datetime

today = datetime.datetime.now()
today = str(today).split(" ")[0]
today = today.replace("-", "")
print(today)

token = "nfijksnfjisdnf"
username = "ahmadimdad"
graph_id = "running1graph"
pixela_endpoint = "https://pixe.la"
pixela_input_endpoint = f"{pixela_endpoint}/v1/users/{username}/graphs/{graph_id}"
pixela_update_endpoint = f"{pixela_endpoint}/v1/users/{username}/graphs/{graph_id}/{today}"
# pixela_graph_endpoint = f"{pixela_endpoint}/v1/users/ahmadimdad/graphs"

# pixel_user_endpoint = f"{pixela_endpoint}/v1/users"
# user_parameters = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

token_header = {
    "X-USER-TOKEN": token
}

# graph_params = {
#     "id": "running1graph",
#     "name": "run-meter",
#     "unit": "kilometers",
#     "type": "float",
#     "color": "kuro",
#     "timezone": "Asia/Karachi"
# }

# make_user_response = requests.post(url=pixel_user_endpoint, json=user_parameters)
# print(make_user_response.text)

# make_graph_response = requests.post(url=pixela_graph_endpoint,
#                                     json=graph_params, headers=token_header)


# input_parameter = {
#     "date": today,
#     "quantity": "1.5",
# }
# input_response = requests.post(url=pixela_input_endpoint,
#                                json=input_parameter, headers=token_header)
# update_params = {
#     "quantity": "0.5"
# }

delete_response = requests.delete(url=pixela_update_endpoint,
                                  headers=token_header)
print(delete_response.text)
