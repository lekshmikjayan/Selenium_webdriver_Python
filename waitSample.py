from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("an")
time.sleep(5)
results = driver.find_element(By.XPATH, "//div[@class='products']/div")
#count = len(results)

#assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
time.sleep(15)