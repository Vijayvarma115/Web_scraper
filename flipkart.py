import requests
from bs4 import BeautifulSoup
import csv 
import pandas as p

url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')

titles=soup.find_all('div',class_='KzDlHZ')
rating=soup.find_all('div',class_='XQDdHH')
reviews=soup.find_all('span',class_='Wphh3N')
prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')

mobile_title=[]
mobile_rating=[]
mobile_reviews=[]
mobile_prices=[]

for title,rat,rev,pri in zip(titles,rating,reviews,prices):
    mobile_title.append(title.text)
    mobile_rating.append(rat.text)
    mobile_reviews.append(rev.text)
    mobile_prices.append(pri.text)

#Saving data into CSV
data={'mobile_title':mobile_title,'mobile_rating':mobile_rating,'mobile_reviews':mobile_reviews,'mobile_prices':mobile_prices}
model=p.DataFrame(data=data)

model.to_csv("mobilesinfo.csv")