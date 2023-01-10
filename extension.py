from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/auth/login")
#link text only used for links provided in anchor tag (<a>)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth(2) input").send_keys("hai@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("hai@1234")
driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click()