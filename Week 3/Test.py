from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service

service = Service(
    executable_path="F:\DSA\Week 3\chromedriver-win64\chromedriver-win64/chromedriver.exe"
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

products = [] 
prices = []  

driver.get("https://www.whatmobile.com.pk/")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll("li", attrs={"class": "product"}):
    print(a)
    name = a.find("a", attrs={"class": "BiggerText"})
    price = a.find("span", attrs={"class": "PriceFont"})
    if name != None and price != None:
        products.append(name["title"])
        prices.append(price.text)
    if len(products) == 50:
        break
df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("product.csv", index=False, encoding="utf-8")