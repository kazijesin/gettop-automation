import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@when("Click right & left arrow of the top banners")
def click_right_left_arrow(context):
    context.app.top_banners.click_right_left_arrow()

@when("User can click bottom dots to see top banners")
def bottom_dots(context):
    context.app.top_banners.bottom_dots()

@when("click on product banner")
def click_product_banner(context):
    context.app.top_banners.click_product_banner()

@then("Verify correct category page opens")
def verify_correct_category_open(context):
    context.app.top_banners.verify_correct_category_open()




