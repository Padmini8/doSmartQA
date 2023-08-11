import time
from behave import *
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User navigated to SmartQA CreateAccount page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/register")
    # context.driver.find_element(By.XPATH, "//div[@id = 'loginCreateAccount']").click()


@when('User should enter mandatory fields')
def step_impl(context):
         # context.driver.find_element(By.XPATH, "//div[@id='firstname']").send_Keys("H")
         # context.driver.find_element(By.XPATH, "//div[@id='lastname']").send_Keys("R")
         context.driver.find_element(By.ID, "firstname").send_keys("H")
         context.driver.find_element(By.ID, "lastname").send_keys("R")
         context.driver.find_element(By.ID, "email").send_keys("stagharikaa@gmail.com")
         context.driver.find_element(By.ID, "username").send_keys("HR")
         context.driver.find_element(By.ID, "organization").send_keys("stagian")
         context.driver.find_element(By.ID, "password").send_keys("Harika@23")
         context.driver.find_element(By.ID, "cpassword").send_keys("Harika@23")
         time.sleep(5)

@then('User should click on the Register Cta')
def step_impl(context):
    # register_cta = context.driver.find_element(By.XPATH, '//div[@id="login-form-submit"]')
    # register_cta = context.driver.find_element(By.ID, "login-form-submit")
    register_cta = context.driver.find_element(By.XPATH, "//*[@id='login-form-submit']")
    # wait = WebDriverWait(context.driver, 10)
    # register_button = wait.until(EC.element_to_be_clickable((By.ID, "login-form-submit")))
    # register_button.click()
    # time.sleep(3)

# Scenario:Creating account without providing the details
# @when('User should not provide any details in the fields')
# def step_impl(context):
#     context.driver.find_element(By.ID, "firstname").send_keys("")
#     context.driver.find_element(By.ID, "lastname").send_keys("")
#     context.driver.find_element(By.ID, "email").send_keys("")
#     context.driver.find_element(By.ID, "username").send_keys("")
#     context.driver.find_element(By.ID, "organization").send_keys("")
#     context.driver.find_element(By.ID, "password").send_keys("")
#     context.driver.find_element(By.ID, "cpassword").send_keys("")
#
# @then('User should get a proper warning message')
# def step_impl(context):
#     expected_warning_message = "Field's can't be empty."
#     assert context.driver.find_element(By.ID, "loginCardTitle").text.__contains__(expected_warning_message)
#     # print(expected_warning_message)
#
# # Scenario:Creating a account with the existing email id
# @when('User should provide the existing email id details')
# def step_impl(context):
#    context.driver.find_element(By.ID, "email").send_keys("harikaramagani@gmail.com")
#
# @then('User should get a proper warning message')
# def step_impl(context):
#     expected_warning_message = "Sorry,email already already exists."
#     assert context.driver.find_element(By.ID, "loginCardTitle").text.__contains__(expected_warning_message)
#     print(expected_warning_message)

