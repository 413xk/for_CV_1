from selenium.webdriver.common.by import By


class ItemPageLocators:
    ADD_TO_BASKET_BUTTON = By.CSS_SELECTOR, '#add_to_basket_form'
    ADDED_ITEM_NAME = By.CSS_SELECTOR, '#messages .alertinner strong'
    ADDED_ITEM_PRICE = By.CSS_SELECTOR, '.alertinner p strong'
    ITEM_NAME = By.CSS_SELECTOR, '.product_main h1'
    ITEM_PRICE = By.CSS_SELECTOR, '.product_main .price_color'
