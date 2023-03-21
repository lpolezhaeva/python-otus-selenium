from selenium.webdriver.common.by import By


class AccountRegisterPage:
    HEADER = (By.CSS_SELECTOR, "h1")
    ACCOUNT_LEGEND = (By.CSS_SELECTOR, "#account > legend")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-confirm")
    NEWSLETTER_RADIO_CHECKED = (By.CSS_SELECTOR, "input[type='radio'][value='1']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "a.agree")
