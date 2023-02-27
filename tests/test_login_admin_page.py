from page_objects.login_admin_page import LoginAdminPage


def test_login_admin_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.PANEL_TITLE)
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)

