from selenium.webdriver.common.by import By


class ProductCardPage:
    HEADER = (By.CSS_SELECTOR, "h1")
    PRODUCT_DETAILS_LIST = (By.CSS_SELECTOR, ".list-unstyled")
    SMALL_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='5']")
    MEDIUM_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='6']")
    LARGE_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='7']")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='8']")
    SECOND_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='9']")
    THIRD_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='10']")
    FORTH_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='11']")
    TEXT_INPUT = (By.CSS_SELECTOR, "#input-option208")
