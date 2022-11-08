from selenium.webdriver.common.by import By


class ItemPageLocators:
    ADD_TO_BASKET_BUTTON = By.CSS_SELECTOR, '#add_to_basket_form'
    ADDED_ITEM_NAME = By.CSS_SELECTOR, '#messages .alertinner strong'
    ADDED_ITEM_PRICE = By.CSS_SELECTOR, '.alertinner p strong'
    ITEM_NAME = By.CSS_SELECTOR, '.product_main h1'
    ITEM_PRICE = By.CSS_SELECTOR, '.product_main .price_color'
    SUCCESS_MESSAGE = By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)'


class BasePageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, '#login_link'
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, '#login_link_inc'
    VIEW_BASKET = By.CSS_SELECTOR, '.btn-group a.btn'


class BasketPageLocators:
    ITEM_IN_BASKET = By.CSS_SELECTOR, '.basket-items'
    EMPTY_BASKET = By.CSS_SELECTOR, '#content_inner p'
