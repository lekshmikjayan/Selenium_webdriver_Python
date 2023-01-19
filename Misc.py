
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service(r'C:\Users\leksh\Downloads\chromedriver_win32\chromedriver.exe');
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
#taking screenshots
driver.get_screenshot_as_file("screen.png")

#head and headless modes - in head mode browser can be seen but in headless mode
# browser cant be seen, test will run in invisible mode, comparing both headless mode is more fast,
#so we need to add options in driver , once it is run, no borwser will be showed up, but test wll be running automatically backgnd

