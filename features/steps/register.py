from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to Register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()

@when(u'I enter mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Raki")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Ramesh")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "anand" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("12345670")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")

@when(u'I select privacy policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()

@when(u'I click on continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

@when(u'I enter details into all fields')
def step_impl(context):
     print("Inside - I enter details into all fields")

@when(u'I enter details into all fields except email field')
def step_impl(context):
     print("Inside - I enter details into all fields except email field")

@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print("Inside - I enter existing accounts email into email field")

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print("Inside - I Proper warning message informing about duplicate account should be displayed")

@when(u'I dont enter anything into the fields')
def step_impl(context):
    print("Inside - I dont enter anything into the fields")

@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    print("Inside - Proper warning messages for every mandatory fields should be displayed ")
