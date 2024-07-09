import requests

sheety_get_api_endpoint = ("https://api.sheety.co"
                           "/5b76d09a20bd625d88943bad5d69f77c/"
                           "flightDeals/prices")
sheety_put_api_endpoint = ("https://api.sheety.co/"
                           "5b76d09a20bd625d88943bad5d69f77c/"
                           "flightDeals/prices")


class DataManager:
    def __init__(self):
        self.bearer_token = {
            "Authorization": "Bearer sarcastic"
        }
        self.gather_data = {}

    def get_destination_info(self):
        response = requests.get(url=sheety_get_api_endpoint,
                                headers=self.bearer_token)
        return response.json()["prices"]

    def update_destination_code(self):
        for city in self.gather_data:
            json = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_put_api_endpoint}/{city["id"]}",
                         headers=self.bearer_token, json=json)