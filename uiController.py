from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
       # time.sleep(200)
        assert checkbox.is_selected()

        break

radiobuttons = driver.find_elements(By.XPATH, "//input[@type = 'radio']")
#print(len(radiobuttons))
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(20)