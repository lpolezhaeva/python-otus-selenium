from page_objects.main_page import MainPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Config:
    SLOW = 20


def test_main_page(browser):
    browser.get(browser.url + "/index.php?route=common/home")
    browser.find_element(*MainPage.SEARCH_INPUT)
    browser.find_element(*MainPage.CART_BUTTON)
    browser.find_element(*MainPage.NAVIGATION_BAR)
    browser.find_element(*MainPage.CONTENT_DIV)
    browser.find_element(*MainPage.PARTNERS_CAROUSEL)

    browser.find_element(*MainPage.CART_BUTTON).click()

    WebDriverWait(browser, Config.SLOW).until(
        EC.visibility_of_element_located(MainPage.EMPTY_SHOPPING_CARD_LABEL)
    )

    WebDriverWait(browser, Config.SLOW).until(
        EC.text_to_be_present_in_element(MainPage.EMPTY_SHOPPING_CARD_LABEL, "Your shopping cart is empty!")
    )

