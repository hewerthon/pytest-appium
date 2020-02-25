from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

checkboxes = driver.find_element_by_xpath("//input[@type='checkbox']").text

print(checkboxes)

print(len(checkboxes))

for checkbox in checkboxes:
    checkbox
    checkbox.click()

driver.close()