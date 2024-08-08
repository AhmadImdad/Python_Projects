import smtplib
import requests

user = "ahmad.imdad007@gmail.com"
password = ""
sheety_endpoint = ("https://api.sheety.co"
                   "/5b76d09a20bd625d88943bad5d69f77c/users/formResponses1")


class NotificationManager:
    def __init__(self):
        self.customer_list = list()
        self.get_customer_emails()

    def get_customer_emails(self):
        header = {
            "Authorization": "Bearer sarcasm"
        }
        response = requests.get(url=sheety_endpoint, headers=header)
        print(response.json())
        temp_list = response.json()["formResponses1"]
        for data in temp_list:
            self.customer_list.append(data["enterYourEmail:"])
        print(self.customer_list)

    def notifier(self, cheap_flight_list):
        for email in self.customer_list:
            for flight in cheap_flight_list:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=user, password=password)
                    connection.sendmail(from_addr=user,
                                        to_addrs=email,
                                        msg="Subject: Cheap Flight Found\n\n"
                                            f"{flight.price} is the price.\n"
                                            f"{flight.origin_code} is the origin code\n"
                                            f"{flight.destination_code} is the destination code\n"
                                            f"{flight.in_date} is the departure date\n"
                                            f"{flight.out_date} is the return date\n"
                                            f"Non-stop: {flight.nonstop}")
