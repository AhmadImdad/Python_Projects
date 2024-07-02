import datetime as dt
import pandas as pd
import smtplib as sm
import random

EMAIL = "ahmad.imdad007@gmail.com"
PASSWORD = ""

now = dt.datetime.now()
day_now = now.day
month_now = now.month
year_now = now.year
flag = True
already_wished_emails = list()


def send_mail(letter, to_email):
    with sm.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=to_email,
                            msg=f"Subject: Happy Birthday\n\n{letter}")


try:
    data = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    exit()
else:
    while flag:

        days_of_birthday = data["day"].to_list()
        months_of_birthday = data["month"].to_list()
        data_to_wish = None
        count = 0

        for days, months in zip(days_of_birthday, months_of_birthday):
            if days == day_now and month_now == months:
                email = data.email[count]
                if email not in already_wished_emails:
                    data_to_wish = data[data["email"] == email]
                    break
            count += 1

        if data_to_wish is not None:
            i = random.randint(1, 3)
            letter_to_send = ""
            name = data_to_wish.name.to_list()
            name = "".join(name)

            with open(file=f"letter_templates/letter_{i}.txt") as file:
                letter_to_send += file.read()

            letter_to_send = letter_to_send.replace("[NAME]", name)
            email = data_to_wish["email"].to_list()
            email = "".join(email)
            already_wished_emails.append(email)
            send_mail(letter_to_send, email)

        else:
            flag = False
