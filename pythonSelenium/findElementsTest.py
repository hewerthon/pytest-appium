from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\IEDriverServer.exe")

# driver.maximize_window()

driver.get("https://makemytrip.com")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From'").send_keys("Del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

driver.close()
