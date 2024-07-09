from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
data = data_manager.get_destination_info()

updated = False
for city in data:
    if city["iataCode"] == "":
        iataCode = flight_search.get_destination_code(city["city"].upper())
        city["iataCode"] = iataCode
        updated = True
data_manager.gather_data = data
if updated:
    data_manager.update_destination_code()

cheapest_flight = list()
updated = False
count = 0
for city in data_manager.gather_data:
    flight_search.non_stop = "true"
    data = flight_search.find_cheap_flight(city)
    if data is None or data == []:
        flight_search.non_stop = "false"
        data = flight_search.find_cheap_flight(city)
    if data is not None and data != []:
        cheapest_flight.append(FlightData.cheapest_info(data, flight_search.non_stop, city["iataCode"]))
        updated = True
if updated:
    notifier = NotificationManager()
    notifier.notifier(cheapest_flight)
    