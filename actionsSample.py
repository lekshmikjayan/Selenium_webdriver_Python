from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#actionchains are used to perform advanced UI interactions
#action.context_click()- right click
#action.double_click(driver.find_element(By.)) -double click

#perform()- used to execute the code

action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()


