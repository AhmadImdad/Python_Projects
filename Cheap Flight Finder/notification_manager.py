import smtplib

user = "ahmad.imdad007@gmail.com"
password = "cxzuskofspvuezsx"


class NotificationManager:

    def notifier(cheap_flight_list):
        for flight in cheap_flight_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=user, password=password)
                connection.sendmail(from_addr=user,
                                    to_addrs=user,
                                    msg="Subject: Cheap Flight Found\n\n"
                                        f"{flight.price} is the price.\n"
                                        f"{flight.origin_code} is the origin code\n"
                                        f"{flight.destination_code} is the destination code\n"
                                        f"{flight.in_date} is the departure date\n"
                                        f"{flight.out_date} is the return date.")
