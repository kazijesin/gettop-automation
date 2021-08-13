from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class TopBanners(Page):
    RIGHT_LEFT_ARROW = (By.CSS_SELECTOR, 'svg.flickity-button-icon')
    BOTTOM_DOTS = (By.CSS_SELECTOR, 'ol.flickity-page-dots')
    PRODUCT_BANNER = (By.CSS_SELECTOR, 'div.flickity-viewport')
    # BANNER_PAGE = (By.CSS_SELECTOR, 'span.divider')
    def click_right_left_arrow(self):
        self.click(*self.RIGHT_LEFT_ARROW)

    def bottom_dots(self):
        self.click(*self.BOTTOM_DOTS)

    def click_product_banner(self):
        self.click(*self.PRODUCT_BANNER)

    # def verify_correct_category_open(self):
    #     self.wait.until(EC.presence_of_element_located(*self.BANNER_PAGE))

    def verify_correct_category_open(self):
        assert "https://gettop.us/product-category/macbook/" in self.driver.current_url, f"url https://gettop.us/product-category/macbook/ not in {self.driver.current_url}"

