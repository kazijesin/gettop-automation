from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from support.logger import logger
#import sys

#sys.setrecursionlimit(10**6)



class Header(Page):
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')

    #class="search-field mb-0" placeholder="Search…" value="" name="s" autocomplete="off">)
    #By.ID, 'woocommerce-product-search-field-0')
    SEARCH_ICON = (By.CSS_SELECTOR, 'i.icon-search')
    CART = (By.ID, 'nav-cart-count')
    ORDER_LINK = (By.ID, 'nav-orders')
    SIGN_IN = (By.CSS_SELECTOR,'h1.a-spacing-small')
    NEW_ARRIVALS = (By.CSS_SELECTOR,'span.nav-a-content')
    FLAG = (By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")
    #FLAG = (By.CSS_SELECTOR,'.icp-nav-flag-us')
    SPANISH =(By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPT_SELECT = (By.ID, 'searchDropdownBox')


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def click_order(self):
        self.click(*self.ORDER_LINK)

    #def find_element(self, *SIGN_IN):
            #self.find_element(*SIGN_IN)

    def hover_over_new_arrivals(self):
        NEW_ARRIVALS = self.driver.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(NEW_ARRIVALS)
        actions.perform()

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_lang_visible(self):
        self.wait_for_element_appear(*self.SPANISH)

    def select_department(self):
        select = Select(self.driver.find_element(*self.DEPT_SELECT))
        select.select_by_value('search-alias=subscribe-with-amazon')




