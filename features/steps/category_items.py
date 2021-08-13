from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when("Click on the categories")
def click_categories(context):
    context.app.product_page.click_categories()


@then('"{text}" message is displayed')
def verify_empty_cart_msg(context, text):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    assert actual_text == text, f'Expected {text}, but got {actual_text}'


@then('Verify {box_count} benefit boxes are displayed')
def verify_benefit_boxes(context, box_count):
    box_count = int(box_count)
    boxes = context.driver.find_elements(By.CSS_SELECTOR, "div.benefit-box")
    assert len(boxes) == box_count, f'Expected {box_count} boxes, but got {len(box_count)}'