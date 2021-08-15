import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@when("Click on a product")
def click_product(context):
    context.app.product_page.click_product()

@when("You may also like block is shown")
def block_is_shown(context):
    context.app.product_page.block_is_shown()

@when ("Click link under the block")
def click_under_block(context):
    context.app.product_page.click_under_block()

@then("Verify it opens the correct page")
def verify_correct_page_opens(context):
    context.app.product_page.verify_correct_page_opens()
