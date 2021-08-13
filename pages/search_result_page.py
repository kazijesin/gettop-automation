from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, 'input#search')
    PRODUCT_RESULT = (By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    SEARCH_RESULT1 = (By.CSS_SELECTOR, 'twotabsearchtextbox')
    PRODUCT_RESULT1 = (By.CSS_SELECTOR, 'span.a-size-base-plus a-color-base a-text-normal')
    GARDEN_SUBNAV = (By.CSS_SELECTOR, 'div.nav-search-facade')
    DEALS_SUBNAV = (By.CSS_SELECTOR, 'div.bxc-grid__image   bxc-grid__image--light')




    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)

    def verify_search_worked(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_garden_department(self):
       self.wait_for_element_appear(*self.GARDEN_SUBNAV)

    def verify_user_see_deals(self):
        self.wait_for_element_appear(*self.DEALS_SUBNAV)






