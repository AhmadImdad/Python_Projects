class FlightData:
    def __init__(self, price, origin_code, destination_code, in_date, out_date, nonstop):
        self.price = price
        self.origin_code = origin_code
        self.destination_code = destination_code
        self.in_date = in_date
        self.out_date = out_date
        self.nonstop = nonstop

    def cheapest_info(data, nonstop, destination_code_):
        min_price = float(data[0]["price"]["grandTotal"])
        index = 0
        count = 0
        for all_data in data:
            if float(all_data["price"]["grandTotal"]) < min_price:
                min_price = float(all_data["price"]["grandTotal"])
                index = count
            count += 1

        price = data[index]["price"]["total"]
        origin_code = data[index]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination_code = destination_code_
        in_date = data[index]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        out_date = data[index]["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        cheapest_flight = FlightData(price, origin_code, destination_code, in_date, out_date, nonstop)
        return cheapest_flight
