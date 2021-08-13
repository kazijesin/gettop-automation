from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when("Click on cart icon")
def click_cart(context):
    context.app.product_page.click_cart()


@then("Verify your cart is currently empty is shown")
def verify_no_products_added_present(context):
    context.app.product_page.verify_no_products_added_present()

@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    context.app.header.verify_cart_count(expected_count)