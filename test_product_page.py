import time

import pytest

from .pages.product_page import ProductPage


# make parametrize, dynamic link and xfail for dropped test
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == '?', reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.delete_all_cookies()  # clear cookies before start
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_product_page()
    product_page.click_button()
    product_page.should_be_correct_answer()
    product_page.should_be_correct_page_data()
