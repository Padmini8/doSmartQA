from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am logged in to SmartQA with username "{username}" and password "{password}"')
def step_login_to_smartqa(context, username, password):
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/")
    # username_field = context.driver.find_element(By.ID, "email")
    # password_field = context.driver.find_element(By.ID, "password")
    # login_button = context.driver.find_element(By.ID, "login-form-submit")
    # username_field.send_keys(username)
    # password_field.send_keys(password)
    # login_button.click()

@given('I am on the dropdown page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/main/projectselect")
    time.sleep(5)

@when('I select option "{option}" from the dropdown')
def step_impl(context, option):
    dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="openExisting"]/div[1]/div/div[1]/div/button/div/div[2]'))
    dropdown_element.click()

@then('The selected option should be "{expected_option}"')
def step_impl(context, expected_option):
    dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="myProjectsList"]/tbody/tr/td'))
    selected_option = dropdown.first_selected_option.text
    assert selected_option == expected_option, f"Expected {expected_option}, but got {selected_option}"

@then('User successfully Logout')
def step_impl(context):
    dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="myProjectsList"]/tbody/tr/td'))
    selected_option = dropdown.first_selected_option.text
