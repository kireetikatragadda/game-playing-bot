from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\\Users\\KISHORE KUMAR\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID,"cookie")


items = driver.find_elements(By.CSS_SELECTOR,"#store div")
print(items)
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

timeout = time.time()+5
five_min = time.time()+60*5
print(timeout)
print(five_min)

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            print(element_text)

            if element_text != "":
                cost = int(element_text.split("-")[1].replace(",",""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        #get current cookie count
        money_element = driver.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",","")

        cookie_count = int(money_element)

        #find upgrades that we can currently afford

        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        #to purchase the most expensive affordable upgrade
        affordable_upgrade = max(affordable_upgrades)

        to_purchase_id = affordable_upgrades[affordable_upgrade]

        driver.find_element(By.ID,to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break









