class FlightData:
    def __init__(self, price, origin_code, destination_code, in_date, out_date):
        self.price = price
        self.origin_code = origin_code
        self.destination_code = destination_code
        self.in_date = in_date
        self.out_date = out_date

    def cheapest_info(data):
        min_price = data[0]["price"]["grandTotal"]
        index = 0
        for all_data in data:
            if all_data["price"]["grandTotal"] < min_price:
                index = all_data.index()
                print(index)
        price = data[index]["price"]["total"]
        origin_code = data[index]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination_code = data[index]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        in_date = data[index]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        out_date = data[index]["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        cheapest_flight = FlightData(price, origin_code, destination_code, in_date, out_date)
        return cheapest_flight
