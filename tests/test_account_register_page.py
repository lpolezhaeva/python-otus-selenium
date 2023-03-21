from page_objects.account_register_page import AccountRegisterPage


def test_account_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*AccountRegisterPage.HEADER)
    browser.find_element(*AccountRegisterPage.ACCOUNT_LEGEND)
    browser.find_element(*AccountRegisterPage.FIRSTNAME_INPUT)
    browser.find_element(*AccountRegisterPage.LASTNAME_INPUT)
    browser.find_element(*AccountRegisterPage.EMAIL_INPUT)
    browser.find_element(*AccountRegisterPage.TELEPHONE_INPUT)
    browser.find_element(*AccountRegisterPage.PASSWORD_INPUT)
    browser.find_element(*AccountRegisterPage.CONFIRM_PASSWORD_INPUT)
    browser.find_element(*AccountRegisterPage.NEWSLETTER_RADIO_CHECKED)
    browser.find_element(*AccountRegisterPage.SUBMIT_BUTTON)
    browser.find_element(*AccountRegisterPage.PRIVACY_POLICY_CHECKBOX)
    browser.find_element(*AccountRegisterPage.PRIVACY_POLICY_LINK)
