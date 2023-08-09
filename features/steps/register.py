from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def before_scenario(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

def after_scenario(context):
    context.driver.quit()

@given(u'I navigate to Register page')
def step_impl(context):
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
    context.driver.find_element(By.ID, "input-firstname").send_keys("Raki")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Ramesh")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "anand" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("12345670")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    context.driver.find_element(By.XPATH,"//input[@name='newsletter']").click()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Raki")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Ramesh")
    context.driver.find_element(By.ID, "input-telephone").send_keys("12345670")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter']").click()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("abc123kk@gmail.com")

@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_warning)

@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"
    assert context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_privacy_policy_warning)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_first_name_warning)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(expected_last_name_warning)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(expected_email_warning )
    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(expected_telephone_warning)
    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(expected_password_warning)










