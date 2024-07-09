import requests
from datetime import datetime, timedelta

amadeus_api_key = "FwQLs9gotRjDvbXpfLaxpAQ8alDuCRFL"
amadeus_api_secret = "757iDQtgdDTq6F3t"
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

FROM = "LONDON"


class FlightSearch:
    def __init__(self):
        self.token_type = ""
        self.token = ""
        self.origin_iata_code = self.get_destination_code(FROM)

    def get_destination_code(self, city_name):
        self.get_token()
        header = {
            "Authorization": f"{self.token_type} {self.token}"
        }
        parameters = {
            "keyword": city_name,
            "max": 1,
            "include": "AIRPORTS"
        }
        response = requests.get(url=iata_endpoint, headers=header, params=parameters)
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print("Index Error!!!!")
            return None
        except KeyError:
            print("Key Error!!!")
            return None
        else:
            return code

    def get_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": amadeus_api_key,
            "client_secret": amadeus_api_secret
        }
        response = requests.post(url=token_endpoint, headers=headers, data=body)
        print(response.json())
        self.token_type = response.json()["token_type"]
        self.token = response.json()["access_token"]

    def find_cheap_flight(self, city):
        temp = datetime.now() + timedelta(days=30)
        departure_date = datetime.now() + timedelta(days=30)
        departure_date = str(departure_date).split(" ")[0]
        return_date = temp + timedelta(days=10)
        return_date = str(return_date).split(" ")[0]
        parameters = {
            "originLocationCode": self.origin_iata_code,
            "destinationLocationCode": city["iataCode"],
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "maxPrice": int(round(city["lowestPrice"])),
        }
        header = {
            "Authorization": f"{self.token_type} {self.token}",
        }
        response = requests.get(url=flight_search_endpoint,
                                headers=header, params=parameters)
        if response.status_code != 200:
            print("Error in Flight Searching!!!!")
            return None
        else:
            return response.json()["data"]
