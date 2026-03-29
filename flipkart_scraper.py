from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup Chrome
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Remove this line to see browser open
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

products_list = []

for page in range(1, 60):
    url = f"https://www.flipkart.com/search?q=laptops&page={page}"
    driver.get(url)

    # Wait for products to load
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.find_all("div", attrs={"data-id": True})

    print(f"Page {page} — Found {len(products)} containers")

    for product in products:
        try:
            name = product.find("div", class_="RG5Slk")
            selling_price = product.find("div", class_="hZ3P6w")
            original_price = product.find("div", class_="kRYCnD")
            discount = product.find("div", class_="HQe8jr")
            rating = product.find("div", class_="MKiFS6")
            rating_count = product.find("span", class_="PvbNMB")

            if name:
                products_list.append({
                    "Product Name": name.text.strip(),
                    "Selling Price": selling_price.text.strip() if selling_price else "N/A",
                    "Original Price": original_price.text.strip() if original_price else "N/A",
                    "Discount": discount.text.strip() if discount else "N/A",
                    "Rating": rating.text.strip()[:3] if rating else "N/A",
                    "Rating Count": rating_count.text.strip() if rating_count else "N/A",
                })
        except Exception:
            pass

    print(f"✅ {len(products_list)} products collected so far")
    time.sleep(2)

driver.quit()

df = pd.DataFrame(products_list)
df.drop_duplicates(subset=["Product Name"], inplace=True)
df.to_csv("flipkart_laptops.csv", index=False)
print(f"\n🎉 Done! {len(df)} products saved!")
print(df.head())