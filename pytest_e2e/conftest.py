from selenium import webdriver
import pytest
import time

# driver = webdriver.Firefox(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\IEDriverServer.exe")

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getOption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\geckodriver.exe")

    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path="C:\\Users\\hewer\\Projects\\pytest-appium\\Drivers\\IEDriverServer.exe")

    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
