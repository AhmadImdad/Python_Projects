import requests
from datetime import timedelta, datetime
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'AC9a6fb4414e6272c653a3df3031584c35'
auth_token = '3ef3b1f0081cca0c570290165d722645'
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "P46FGZ0Y47Z5L9FQ"
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
cause_event = False
try:
    stock_dates = response.json()["Time Series (Daily)"]
except KeyError:
    print("Key error")
    exit()
else:
    data_list = [values for (key, values) in stock_dates.items()]
    close_rate_yesterday = float(data_list[0]["4. close"])
    close_rate_day_before_yest = float(data_list[1]["4. close"])
    difference_rate = (abs(close_rate_yesterday - close_rate_day_before_yest)
                       / close_rate_yesterday) * 100
    change = close_rate_yesterday - close_rate_day_before_yest
    if change > 0:
        change = "up"
    else:
        change = "down"
    if difference_rate >= 2:
        cause_event = True

if cause_event:
    today = datetime.now() - timedelta(days=1)
    today = str(today).split(" ")[0]
    news_parameters = {
        "apikey": "475b12e157a34c32a570ff3da07ec21f",
        "q": COMPANY_NAME,
        "from": today
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    title1 = response.json()["articles"][0]["title"]
    description1 = response.json()["articles"][0]["description"]
    title2 = response.json()["articles"][1]["title"]
    description2 = response.json()["articles"][1]["description"]
    title3 = response.json()["articles"][2]["title"]
    description3 = response.json()["articles"][2]["description"]
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to="whatsapp:+923187085897",
        body=f"Tesla stock {change} by {difference_rate}%"
             f"\nNews"
             f"\nTitle:\n\n{title1}"
             f"Description:\n\n{description1}"
             f"\nTitle:\n\n{title2}"
             f"Description:\n\n{description2}"
             f"\nTitle:\n\n{title3}"
             f"Description:\n\n{description3}"
    )
