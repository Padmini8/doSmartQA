from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I navigated to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("abc123kk@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("abc123@")

@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()

@then(u'I should get loggen in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    context.driver.quit()

@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "anand" + time_stamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(invalid_email)
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("abc123@")

@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert expected_warning_message in context.driver.find_element(By.CLASS_NAME, "alert.alert-danger.alert-dismissible").text

@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("abc123rk@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("abc123@rku")

@when("I dont anything into email and password fields")
def dont_enter_credentials(context):
    # Implement the code to not enter anything into email and password fields
    pass

@when("I enter invalid email and invalid password into the fields")
def enter_invalid_email_and_invalid_password(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "anand" + time_stamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(invalid_email)
    context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("abc123@1123")

@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert expected_warning_message in context.driver.find_element(By.CLASS_NAME, "alert.alert-danger.alert-dismissible").text










