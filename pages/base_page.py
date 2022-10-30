from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .locators import ItemPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_button(self):
        url = self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET_BUTTON)
        url.click()

 #   def find_element(self, what):
  #      return self.browser.find_element(By.CSS_SELECTOR, what)

