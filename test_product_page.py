import pytest

from .pages.product_page import ProductPage

# make parametrize, dynamic link and xfail for dropped test
'''@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == '?', reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.delete_all_cookies()  # clear cookies before start
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_product_page()
    product_page.click_button_add_to_basket()
    product_page.should_be_correct_answer()
    product_page.should_be_correct_page_data()
'''


@pytest.mark.xfail(reason='fix it later')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.click_button_add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url, 0)
    product_page.open()
    product_page.should_not_be_success_message()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.should_be_login_link()
    page.go_to_login_page()
    page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason='fix it later')
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.click_button_add_to_basket()
    product_page.should_success_message_disappear()
