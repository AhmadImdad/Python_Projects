import requests
import datetime
import smtplib

MY_LAT = 31.450365
MY_LONG = 73.134964
user = "ahmad.imdad007@gmail.com"
password = "cxzuskofspvuezsx"

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
latitude = float(iss_response.json()["iss_position"]["latitude"])
longitude = float(iss_response.json()["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}
response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split(":")[0]
AM_PM = response.json()["results"]["sunrise"].split(" ")[1]
if AM_PM == "PM":
    sunrise = str(int(sunrise) + 12)
sundown = response.json()["results"]["sunset"].split(":")[0]
AM_PM = response.json()["results"]["sunset"].split(" ")[1]
if AM_PM == "PM":
    sundown = str(int(sundown) + 12)

sundown = int(sundown)
sunrise = int(sunrise)
now = datetime.datetime.now()
hour = now.hour
print(hour, sundown, sunrise)


def mailer():
    if abs(latitude - MY_LAT) <= 5 and abs(longitude - MY_LONG) <= 5:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user,
                                to_addrs=user,
                                msg="Subject: ISS Satelite Overhead Alert\n\n"
                                    "You can see the ISS satellite"
                                    " right above in the sky right now!")


if 23 >= hour > sundown:
    mailer()
elif 0 <= hour <= sunrise:
    mailer()
