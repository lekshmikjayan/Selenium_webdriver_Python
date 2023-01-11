import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ua")
time.sleep(10)
countries= driver.find_elements(By.CSS_SELECTOR,"li[class = 'ui-menu-item']a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
#wen u update value through script, we cud extract text "get_attribute" method
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"