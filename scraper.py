import requests
from bs4 import BeautifulSoup
import smtplib 

URL1='https://www.amazon.in/Skechers-Black-Performance-Refine-Running/dp/B01N6STMQY/ref=sr_1_3?dchild=1&keywords=skechers%2B600&qid=1598200988&sr=8-3&th=1&psc=1'
URL2='https://www.amazon.in/Skechers-Track-Field-Shoes-6-55074-NVY/dp/B07PPFBLSL/ref=sr_1_1?dchild=1&keywords=skechers%2B600&qid=1598200988&sr=8-1&th=1&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

page1=requests.get(url=URL1,headers=headers)
page2=requests.get(url=URL2,headers=headers)

soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')

#Calculate Price1
price1 = soup1.find(id='priceblock_ourprice')
if price1 is None:
    price1=soup1.find(id='priceblock_dealprice')
price1=price1.get_text()

#calculate Price2
price2 = soup2.find(id='priceblock_ourprice')
if price2 is None:
    price2=soup2.find(id='priceblock_dealprice')
price2=price2.get_text()

convertedPrice = (float(price1[2:7].replace(',','')),float(price2[2:7].replace(',','')))

def send_mail(x):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('vermapankaj1997@gmail.com','htfwxstbiripexup')

    subject = 'Price Fell Down!!'
    if x==0:
        body = 'Ye wala Black - Rishu ki pasand-  https://www.amazon.in/Skechers-Black-Performance-Refine-Running/dp/B01N6STMQY/ref=sr_1_3?dchild=1&keywords=skechers%2B600&qid=1598200988&sr=8-3&th=1&psc=1'
    else:
        body = 'Ye hai Go Run 600 -  https://www.amazon.in/Skechers-Track-Field-Shoes-6-55074-NVY/dp/B07PPFBLSL/ref=sr_1_1?dchild=1&keywords=skechers%2B600&qid=1598200988&sr=8-1&th=1&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'vermapankaj1997@gmail.com',
        'vermapankaj1997@gmail.com',
        msg
    )
    server.quit()

def checkIT():
    x=0
    for i in convertedPrice:
        if i < 2700:
            send_mail(x)
        x=x+1

checkIT()