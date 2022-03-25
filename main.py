from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from sqlalchemy import create_engine
import pandas as pd
import openpyxl
import json
import time

# Function to verify the age -

def age_verification():
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="agree-button"]')))
    driver.find_element(By.XPATH, '//button[@class="agree-button"]').click()
    time.sleep(5)


# Function to get all links of products from given website

def get_links():
    condition = True
    while condition:
        productList = driver.find_elements(By.XPATH, '//a[@class="product-item-link"]')
        for dt1 in productList:
            ld1 = dt1.get_property("href")
            print(ld1)
            productLinks.append(ld1)

        try:
            np = driver.find_elements(By.XPATH, '//a[@class="action  next"]')
            np[-1].click()
            # Used time.sleep to get some time to load the complete webpage
            time.sleep(10)
        except:
            condition = False


# Function to get information / data from each link -

def get_info(url):
    driver.get(url)

    time.sleep(2)

    productName2 = ""
    volume = ""
    catagory = ""
    price = ""
    brand = ""

    try:
        productName2 = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[1]/h1/span').text
    except:
        print("Product Name not found for - ", url)

    try:
        volume_tc = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[4]/td').text.replace("ml", "").replace("8 X ", "")
        volume = int(volume_tc) / 10
    except:
        print("Volume Not found for - ", url)

    try:
        catagory = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[5]/td').text
    except:
        print("Catagory not Found for - ", url)

    try:
        price = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/main/div[2]/div/div[3]/div[3]/div[1]/span[2]/span/span[2]').text
    except:
        print("Price not found for - ", url)

    try:
        brand = driver.find_element(By.XPATH, '//*[@id="product-attribute-specs-table"]/tbody/tr[1]/td').text
    except:
        print("brand not found for - ", url)

    tempV = {
        "Sr No.": len(finalData) + 1,
        "Site": "Cellarbration",
        "Product Name": productName2,
        "Quantity": 1,
        "Volume": volume,
        "Category": catagory,
        "Brand": brand,
        "Price": price,
        "Product Link": url}

    finalData.append(tempV)

    # Used time.sleep to get some time to load the complete webpage
    time.sleep(2)


# Driver Code -

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')                   # For Google Colab   (Uncomment in Google Colab)

# driver = webdriver.Chrome('chromedriver', options=options)        # For Google Colab   (Uncomment in Google Colab)

driver = webdriver.Chrome(ChromeDriverManager().install())          # For IDE (Uncomment in IDE)

driver.get("https://cellarbration.com.sg/whiskies.html?product_list_limit=60")

print(">> ", driver.title)

age_verification()

finalData = []
productLinks = []

get_links()

for lnk2 in productLinks:
    get_info(lnk2)

    print("Final Data :- ", finalData[-1])
    print("No of Product Info. :- ", len(finalData))

driver.quit()


# Saving the Data to Excel Sheet -
df = pd.DataFrame.from_dict(finalData)
df.to_excel('finalData_1.xlsx')


# To Save Data in JSON file -
def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_data("Final_Data.json", finalData)


try:
    # To Store Scraped Data in MYSQL Database -
    """
    1) Start MYSQL / PHPMYADMIN Server on Localhost
    2) Create New Data Base - task_data (For Loalhost) or engine = create_engine("mysql+pymysql://<username>:<password>@<hostname>/<Database Name>") for Remote Database)
    """
    engine = create_engine("mysql+pymysql://root:@localhost/task_data")
    df = pd.read_json("Final_Data_test.json")
    df.to_sql("scraped_data", con=engine, if_exists="replace", index=False)
except:
    print("Cannot connect to Database")
