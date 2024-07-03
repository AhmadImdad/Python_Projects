import requests
parameters = {
    "amount": 10,
    "type": "boolean"
}
data_response = requests.get("https://opentdb.com/api.php", params=parameters)
data_response.raise_for_status()
question_data = data_response.json()["results"]
