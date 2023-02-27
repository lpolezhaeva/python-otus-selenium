from selenium.webdriver.common.by import By


class LoginAdminPage:
    PANEL_TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.CSS_SELECTOR, "#footer > a")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    