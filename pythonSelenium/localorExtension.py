from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe")

driver.get("https://login.saleforce.com/")

driver.maximize_window()

driver.find_element_by_css_selector("#username").send_keys("Hewerthon Adalberto")
driver.find_element_by_css_selector(".password").send_keys("Hew")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password").click()

driver.find_element_by_xpath("//a[text()='Cancel'").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
