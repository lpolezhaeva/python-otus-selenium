from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "[name='search']")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")
    NAVIGATION_BAR = (By.CSS_SELECTOR, "ul.nav.navbar-nav")
    CONTENT_DIV = (By.CSS_SELECTOR, "#content")
    PARTNERS_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    EMPTY_SHOPPING_CARD_LABEL = (By.CSS_SELECTOR, "p.text-center")
