from page_objects.product_card_page import ProductCardPage


def test_product_card_page(browser):
    browser.get(browser.url + "/component/monitor/test")
    browser.find_element(*ProductCardPage.HEADER)
    browser.find_element(*ProductCardPage.PRODUCT_DETAILS_LIST)
    browser.find_element(*ProductCardPage.SMALL_RADIO)
    browser.find_element(*ProductCardPage.MEDIUM_RADIO)
    browser.find_element(*ProductCardPage.LARGE_RADIO)
    browser.find_element(*ProductCardPage.FIRST_CHECKBOX)
    browser.find_element(*ProductCardPage.SECOND_CHECKBOX)
    browser.find_element(*ProductCardPage.THIRD_CHECKBOX)
    browser.find_element(*ProductCardPage.FORTH_CHECKBOX)
    browser.find_element(*ProductCardPage.TEXT_INPUT)
