import time
import requests
from bs4 import BeautifulSoup
import smtplib
import urllib.request
import lxml
MY_EMAIL = "testimony9001@gmail.com"
MY_PASS = "Hello$123"
Headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'Accept-Language':"en-US,en;q=0.9",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate"
    # "Cookie":"PHPSESSID=nt0jrn1l833gka7get59hgjjl2",
}

URL = "https://www.amazon.in/Google-Pixel-Black-128GB-Storage/dp/B08H8VZ6PV/ref=sr_1_1?keywords=google+pixel+4a+5g&qid=1663362442&sprefix=google+pixel+4a%2Caps%2C370&sr=8-1"
response = requests.get(URL, headers=Headers)


soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
instant_price = soup.find(name="span", class_="a-price-whole")
price = (instant_price.getText())
print(price)
ml = price.split(",")
ml2 = ml[1].split(".")
# print(ml[0])
# print(ml2[0])
p = int(ml[0])
l = int(ml2[0])
netprice = p * 1000 + l
print(netprice)
myprice = int(34590)
while True:
    time.sleep(60)
    if netprice <= myprice:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Purchase Time\n\nThe phone is available at your set price. Go purchase now."
        )