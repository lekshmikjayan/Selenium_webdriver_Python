
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
browserSortedVeg = []
service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#xpath based on text can be written as
driver.find_element(By.XPATH, "//span[text() = 'Veg/fruit name']").click()
vegWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in vegWebElements:
    browserSortedVeg.append(ele.text)

originalBrowserSortedList = browserSortedVeg.copy

browserSortedVeg.sort()

assert originalBrowserSortedList == browserSortedVeg
