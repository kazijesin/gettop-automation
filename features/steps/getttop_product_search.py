from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# @given ("Open gettop page")
# def open_gettop(context):
#  context.app.main_page.open_main()
#
#
# @when('input {search_word} in search field')
# def search_gettop(context, search_word):
#     context.app.header.input_search(search_word)
#
# @when("Click on gettop search icon")
# def click_search(context):
#     context.app.header.click_search()
#
# @then("Verify search worked for {expected_text}")
# def verify_search_worked(context,expected_text):
#      context.app.search_result_page.verify_search_worked()
#
