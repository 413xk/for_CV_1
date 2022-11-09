import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from .locators import ItemPageLocators, BasePageLocators


class BasePage:
    # 7/11 delete timeout
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_button_add_to_basket(self):
        url = self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET_BUTTON)
        url.click()

    def go_to_basket(self):
        url = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        url.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        self.browser.implicitly_wait(10)
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'login link is not presented'

 #   def find_element(self, what):
  #      return self.browser.find_element(By.CSS_SELECTOR, what)

