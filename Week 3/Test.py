from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time

service = Service(
    executable_path="F:\DSA\Week 3\chromedriver-win64\chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = [] 
prices = []  

driver.get("https://clayaura.pk/shop/")
# time.sleep(5)

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll("div", attrs={"class": "product-wrapper"}):
    print(a)
    name = a.find("h2", class_="wd-entities-title")
    price = a.find("div", class_="woocommerce-Price-amount amount")
    if name != None and price != None:
        products.append(name["title"])
        prices.append(price.text)
    if len(products) == 50:
        break
df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("product.csv", index=False, encoding="utf-8")