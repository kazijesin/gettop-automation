from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given ("Open gettop page")
def open_gettop(context):
    context.app.main_page.open_main()

@when ('Click orders')
def click_orders(context):
    orders_link = context. driver.find_element(By.ID, 'nav-orders')
    orders_link.click()

@when("Click sign in popup")
def click_sign_in_btn(context):


 @when('input {search_word} in search field')
 def search_gettop(context, search_word):
    #context.driver.find_element(By. ID, 'twotabsearchtextbox').send_keys('Table')
    context.app.header.input_search(search_word)

sleep (5)

@when("Click on gettop search icon")
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.header.click_search()

sleep(5)


@when("Click on cart icon")
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify cart has {expected_count} items')
def verify_cart_count(context,expected_count):
 items_in_cart = context.driver.find_element(By.ID,'nav-cart-count')

 @then("Verify search worked for {expected_text}")
 def verify_search_worked(context,expected_text):
     '''actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
     expected_result = 'Table'
     assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
     '''
     context.app.search_result_page.verify_search_worked()

     # @given("Open Gettop page")
     # def open_gettop(context):
     #     context.app.main_page.open_main()

     @when("Click Gettop Orders link")
     def click_order(context):
         # orders_link = context. driver.find_element(By.ID, 'nav-orders')
         context.app.header.click_order()

     @then("Verify page has {expected_text}")
     def verify_search_worked_1(context, expected_text):
         context.app.search_result_page.verify_search_worked_1(expected_text)


