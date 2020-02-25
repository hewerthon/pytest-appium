from selenium.webdriver.common.by import By


class ConfirmPage:
    shop=(By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return self.driver.find_element(*ConfirmPage.shop)
