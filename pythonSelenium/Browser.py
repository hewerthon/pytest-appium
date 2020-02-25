from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\IEDriverServer.exe")

driver.maximize_window()

# driver.get("https://rahulshettyacademy.com/")
#
# print(driver.title)
# assert 'Rahul Shetty Academy' in driver.title
# print(driver.current_url)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.back()
# driver.refresh()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("Hewerthon Adalberto")
driver.find_element_by_name("email").send_keys("hewerthon@outlook.com")
# elem.send_keys('Hewerthon Souza' + Keys.RETURN)
driver.find_element_by_id("exampleCheck1").click()

drop_down = Select(driver.find_element_by_id("exampleFormControlSelect1"))
drop_down.select_by_visible_text("Female")

# dropdown.select_by_index(0)
# dropdown.select_by_value("Male")

driver.find_element_by_id("inlineRadio1")
driver.find_element_by_id("inlineRadio2")

driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)

message = driver.find_element_by_class_name("alert-success").text
assert "Success" in message

# driver.close()
