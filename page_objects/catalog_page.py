from selenium.webdriver.common.by import By


class CatalogPage:
    HEADER = (By.CSS_SELECTOR, "h2")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    COMPARE_TOTAL_LINK = (By.CSS_SELECTOR, "#compare-total")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIMIT_INPUT = (By.CSS_SELECTOR, "#input-limit")
