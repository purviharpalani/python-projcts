import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url="https://www.amazon.in/realme-Storage-Display-Charger-Variant/dp/B09WYW1WWL/ref=sr_1_7?qid=1663949854&refinements=p_36%3A1318505031&rnid=1318502031&s=electronics&sr=1-7"
header = {
    'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=header)
website_html= response.text
soup = BeautifulSoup(website_html, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").get_text()
# print(price)

price_without_currency = price.split("₹")[1]
price_without_currency = price_without_currency.replace(',','')
# print(price_without_currency)

price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find(name="span", id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 9000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_without_currency}"

    with smtplib.SMTP("outlook.office365.com",port=587) as connection:
        connection.starttls()
        result = connection.login("michael.scott.123@outlook.com", "MichaelScott@123*")
        connection.sendmail(
            from_addr="michael.scott.123@outlook.com",
            to_addrs="michael.scott.123@outlook.com",
            msg=f"Suject:Amazon Price Alert!\n\n{message.encode('utf-8')}\n{url}"
        )