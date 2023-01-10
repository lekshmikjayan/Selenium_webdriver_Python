from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome
service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj)

#accessing url
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("hai@gmail.com")
#send_keys are used to send text to any field
driver.find_element(By.ID, "exampleInputPassword1").send_keys(1234567);

driver.find_element(By.ID,"exampleCheck1").click()
#selenium supporing locators: ID, Xpath, css selecytr, name,classname, linkText

#to create xpath for any element //tagname ie, input,h, p etc //syntax tagname[@attribute = 'value']
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Lekshmi")
#driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

#static dropdown =>  fixed options (eg.gender, Y/N), whereas dynamic is dropdown based on the text we enter
#use SELECT class for dropdown
dropdown = Select(driver.find_element((By.ID, "exampleFormControlSelect1")))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)

driver.find_element(By.XPATH,"//input[@type ='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
#assertion will keep validsation and returns error if failed
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hai lekshmi..")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()