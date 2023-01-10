from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chromedriver- is responsible for invoking browser bcz in selenium we cant invoke browser directly
service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.w3schools.com/python/python_functions.asp")
#opens the browser - get

#closes the browser - close
print(driver.title)
print(driver.current_url)

driver.get("https://www.youtube.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
#driver.close()
#webdrvr-class, chrome-method, service=-ppty, creating srvc obj
#service("path to proxy chromedriver"), once it is called, assigned to srvc-obj, tat will be passed to webdrvr ppty
#now chrome helps to access data, and assigned to driver obj, which hold chrome brwsr

