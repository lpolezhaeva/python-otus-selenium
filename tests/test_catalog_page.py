from page_objects.catalog_page import CatalogPage


def test_catalog_page(browser):
    browser.get(browser.url + "/desktops")
    browser.find_element(*CatalogPage.HEADER)
    browser.find_element(*CatalogPage.LIST_VIEW_BUTTON)
    browser.find_element(*CatalogPage.GRID_VIEW_BUTTON)
    browser.find_element(*CatalogPage.COMPARE_TOTAL_LINK)
    browser.find_element(*CatalogPage.SORT_INPUT)
    browser.find_element(*CatalogPage.LIMIT_INPUT)
