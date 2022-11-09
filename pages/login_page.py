import string
import string
import time
from random import choice, randint

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


def login_and_password_generator():
    letters_uppers_and_digits = string.ascii_letters + string.digits
    letters_and_digits = string.ascii_lowercase + string.digits
    password = ''.join(choice(letters_uppers_and_digits) for _ in range(randint(9, 15)))
    email = ''.join(choice(letters_uppers_and_digits) for _ in range(randint(4, 6))) + '@' + \
            ''.join(choice(letters_and_digits) for _ in range(randint(4, 6))) + '.' + \
            ''.join(choice(string.ascii_lowercase) for _ in range(randint(2, 3)))
    return email, password


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        register_email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email_address.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


