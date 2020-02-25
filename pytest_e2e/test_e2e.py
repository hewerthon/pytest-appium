from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.mark.usefixtures("setup")
from pageObjects.HomePage import HomePage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        self.driver.find_element_by_css_selector("a[href*='shop']").click()
        cards = self.driver.find_element_by_css_selector(".card-title a")
        i = -1
        '''for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            #if cardText == "Blackberry":'''



