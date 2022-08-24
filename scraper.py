#Install packages requests and bs4
import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Variable with url for product page
URL = 'https://www.jumia.co.ke/sony-computer-entertainment-ps4-slim-500gb-with-fifa20-bundle-26623878.html'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

def check_discount():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #scrapes product title
    title = soup.find(attrs= {"-fs20 -pts -pbxs"}).get_text()
    #scrapes product discount on page
    discount = soup.find(attrs= {"bdg _dsct _dyn -mls"}).get_text()
    #convert the scraped string to integer
    converted_discount = int(discount[0:2])

    print(title)
    print(converted_discount)
    #insert own requirement
    if (converted_discount > 25):
        send_mail()


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #Insert your sender email and generated app password after activating 2FA on current device.
    server.login('sender email','password')

    subject = 'Discount is now larger'
    body = "Check the jumia link https://www.jumia.co.ke/sony-computer-entertainment-ps4-slim-500gb-with-fifa20-bundle-26623878.html"

    msg = f"Subject: {subject}\n\n{body}"

    #Insert sender and destination email
    server.sendmail(
        'sender email',
        'destination email',
        msg
    )
    print("EMAIL SENT")

    server.quit()

while(True):
    check_discount()
    #this checks the discount every 24 hours(86400 seconds)
    time.sleep(86400)
