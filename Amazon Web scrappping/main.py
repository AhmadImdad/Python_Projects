import requests
from bs4 import BeautifulSoup
import smtplib
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-66981a9c-6f0b0f6b2fb94d5e5c7b5a4c"
  }
EMAIL = "ahmad.imdad009@gmail.com"
PASSWORD = ""
PRODUCT = "INSTANT POT"
response = requests.get(url="https://www.amazon.com/SAMSUNG-Processor-Touchscreen-NP960XGK-KG1US-Moonstone/dp/B0CQ3VXJ3J/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.3b8e83c9-3c43-44b5-841c-814032918d4f&dib=eyJ2IjoiMSJ9.FZySsK-jxok2plvKN5Q6-ikTTjebrBA_UIaFx0hpmdm-FCZid2zbQ7nqE-UeeOHnvEjcD740_DZA3kgIPo9xshLsPMXoeor5nV7tTcJawze8mlsJ7aaSAynlDXBpL8YHj9CFOWH7HGpMK0oZNXTphQ.z4pEWfJscx1yTKmDCIWDJD9eUHotSdEtLcv0Mfl7hMY&dib_tag=se&keywords=computers&pd_rd_r=587b7fe7-a13d-4270-9789-ef8bced7f2ae&pd_rd_w=WMdCe&pd_rd_wg=A838U&pf_rd_p=3b8e83c9-3c43-44b5-841c-814032918d4f&pf_rd_r=4H4KA8ZE2R70JC80YS10&qid=1721242531&refinements=p_n_deal_type%3A23566065011&sr=8-1&th=1", headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
price += soup.find(name="span", class_="a-price-fraction").getText()
price = float(price)

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: {PRODUCT} price Drop!!!"
                                f"\n\n{PRODUCT} price has decreased to {price}.")
