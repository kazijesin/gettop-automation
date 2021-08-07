from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CATEGORY_LINKS = (By.XPATH, "//a[contains(@href,'https://gettop.us/product-category/accessories/')]")
#CATEGORY_LINKS = (By.XPATH, "div= product-category col is-selected")
CATEGORY = (By.CSS_SELECTOR, 'nav.woocommerce-breadcrumb breadcrumbs uppercase')

# @given ("Open Gettop page")
# def open_gettop(context):
#     context.app.main_page.open_main()

@when ("{expected_text} text is shown")
def expected_text(context, expected_text):
    context.driver.find_elements(By.CSS_SELECTOR, 'span.section-title-main')

@when ("Expected {expected_links} categories are shown")
def expected_links(context, expected_links):
    actual_links =context.driver.find_elements((By.XPATH, "div= product-category col is-selected"))
    assert len(actual_links) == int(expected_links), f'Expected{expected_links}, but got {len(actual_links)}'

@then('User can click on each category and Verify correct page opens')
def click_thru_category(context):
    category_links = context.driver.find_elements(*CATEGORY_LINKS)

    for x in range(len(category_links)):
        link = context.driver.find_elements(*CATEGORY_LINKS)[x]

        link_text = link.text
        link.click()

        category_text = context.driver.find_elements(*CATEGORY.text)
        assert link_text in category_text, f'Expected{link_text} not in {category_text}'
