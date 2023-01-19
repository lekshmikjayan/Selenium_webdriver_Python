import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened=driver.window_handles

#windowhandles collects the info regarding all the windows opened and ....
#store it as a list as index number as the order in which windows are opened

driver.switch_to.window(windowsOpened[1])
#switch to child window 4 selenium to undstnd
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.close()

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text