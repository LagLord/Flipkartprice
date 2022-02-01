from bs4 import BeautifulSoup
import requests
from products import product_list
import smtplib

USERNAME = "paadreincarnate@gmail.com"
PASSWORD = "Alman321"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
}

for product in product_list:
    response = requests.get(product_list[product]["link"], headers=headers)
    data = BeautifulSoup(response.text, "html.parser")

    # converting price to int and removing "₹" and ","
    current_price = data.find(name="div", class_="_30jeq3 _16Jk6d").text
    current_price= current_price.replace("₹","")
    current_price = int(current_price.replace(",", ""))
    if current_price <= product_list[product]["price"]:
        message = f"The price of {product} is {current_price} today.\n" \
                  f"Check here: {product_list[product]['link']}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD,)
            connection.sendmail(from_addr=USERNAME, to_addrs="moinkhan42993@gmail.com",
                                msg=f"Subject:Buy Time!\n\n{message}")


