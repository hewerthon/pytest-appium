from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("headless")

driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

