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