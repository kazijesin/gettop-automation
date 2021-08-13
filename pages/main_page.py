from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger



class Main(Page):
    def open_main(self):
        #logger.info('Opening the url https://www.amazon.com/gp/product/B074TBCSC8')
        self.open_url(url='https://gettop.us/')

    # def open_product_page(self):
    #     self.open_url(url='https://www.amazon.com/gp/product/B074TBCSC8')