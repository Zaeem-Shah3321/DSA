from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your ChromeDriver
service = Service(executable_path="F:/DSA/Week 3/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Initialize Chrome options and disable SSL certificate errors
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
options.add_argument("--ignore-ssl-errors")  # Ignore SSL handshake errors

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage
driver.get("https://clayaura.pk/shop/")

# Wait for the products to load dynamically (wait for the container of products)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "products"))  # Wait until the product container is present
    )
except Exception as e:
    print(f"Error: {e}")
    driver.quit()

# Give the page additional time to ensure content is fully loaded
time.sleep(3)

# Get the page source
content = driver.page_source

# Parse the content using BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Lists to store product names and prices
products = []
prices = []
for a in soup.findAll("div", attrs={"class": "product-element-bottom"}):
    name = a.find("h2", class_="woocommerce-loop-product__title")
    price = a.find("span", class_="woocommerce-Price-amount")
    if name and price:
        products.append(name.text.strip())
        prices.append(price.text.strip())
    if len(products) == 50:
        break
driver.quit()
df = pd.DataFrame({"Product Name": products, "Price": prices})
df.to_csv("pr.csv", index=False, encoding="utf-8")
print(df)
