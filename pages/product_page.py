from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Page):
    CART_BTN = (By.CSS_SELECTOR, 'span.header-cart-title')
    NO_PRODUCTS = (By.CSS_SELECTOR, 'p.p.woocommerce-mini-cart__empty-message')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CATEGORIES = (By.CSS_SELECTOR, 'a.nav-top-link')
    SIZE_TOOLTIP = (By.ID, 'a-proper-content-1')
    SIZE_SELECTION_BTN = (By. ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0' )
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox_feature-div')
    SELECTED_CATEGORY = (By.CSS_SELECTOR, 'a.nav-top-link')
    PRODUCT = (By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail size-woocommerce_thumbnail')


    def click_product(self):
        self.click(*self.PRODUCT)


    def click_cart(self):
        self.click(*self.CART_BTN)

    def verify_no_products_added_present(self):
        #self.wait_for_element_appear(*self.NO_PRODUCTS)
        self.wait.until(EC.presence_of_element_located(*self.NO_PRODUCTS))

    def click_categories(self):
        expected_caterogies = ['MAC', 'IPHONE', 'IPAD','WATCH', 'ACCESSORIES']
        caterogies = self.find_elements(*self.CATEGORIES)

        for i in range(len(caterogies)):
         caterogies[i].click()
        self.verify_text(expected_caterogies[i], *self.SELECTED_CATEGORY)



    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BTN)
        self.click(*self.SIZE_OPTION_0)
        self.wait_for_element_appear(*self.PRICE_BUY_BOX)


