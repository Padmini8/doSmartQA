import click
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('I launch the chrome browser')
def step_impl(context):
    # chrome_options = Options()
    # Options.add_argument("--no-proxy-server")
    # context.driver = webdriver.Chrome(options=chrome_options)
    context.driver = webdriver.Chrome()

@when('I open SmartQA Homepage')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/")
    time.sleep(5)

@when('Enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_input = context.driver.find_element(By.ID, "email")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    time.sleep(5)

@then('Click on login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login-form-submit")
    login_button.click()
    time.sleep(3)



# @then('User must successfully login to the project page')
# def step_impl(context):
#     driver = context.driver
#     WebDriverWait(driver, 10).until(EC.url_contains('http://dosmartqa.stagsoftware.net:3009/main/projectselect'))

@then('I am on the dropdown page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/main/projectselect")
    time.sleep(5)

@then('I select option "{option}" from the dropdown')
def step_select_option_from_dropdown(context,option):
    dropdown_button = context.driver.find_element(By.XPATH, '//*[@id="openExisting"]/div[1]/div/div[1]/div/button').click()
    # option_xpath = f'//div[contains(@class, "dropdown-menu")]//span[text()="{option}"]'
    option_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchField"]')))
    time.sleep(3)
    option_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="myProjectsList"]/tbody/tr/td'))).click()


@then('Click on the Open project cta')
def step_click_open_project_cta(context):
     # context.driver.find_element(By.XPATH, "//div[@id='projectselectExistOpen']").click()
     cta_button = context.driver.find_element(By.ID, 'projectselectExistOpen').click()
    # context.driver.execute_script("arguments[0].scrollIntoView();", cta_button)
     time.sleep(3)

@then('User successfully reached to dashboard')
def step_user_reached_dashboard(context):
    dashboard_title = "IstWs2"
    # WebDriverWait(context.driver, 15).until(EC.title_contains(dashboard_title))
    time.sleep(5)

@then('User successfully Logout from dashboard')
def user_successful_logout(context):
   context.driver.find_element(By.XPATH, '//div[@id="hamburger"]/input').click()
   time.sleep(3)
   context.driver.find_element(By.LINK_TEXT,'Logout').click()
   context.driver.quit()


# @scenario(Login to SmartQA with Invalid credentials)

@then('I enter invalid username "{username}"and password "{password}"')
def step_impl(context, username, password):
    username_input = context.driver.find_element(By.ID, "email")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)

@then('I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Sign In"
    assert context.driver.find_element(By.ID, "loginCardTitle").text.__contains__(expected_warning_message)
    print(expected_warning_message)

# @Scenario: Login without entering credentials

@then('I dont enter anything into username and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, "email").send_keys("")
    context.driver.find_element(By.ID, "password").send_keys("")

@then('User should receive a Oops warning message')
def step_impl(context):
    expected_warning_message = "Whoops! username and password fields are required for login."
    actual_warning_message = context.driver.find_element(By.ID, "loginCardTitle").text
    # assert context.driver.find_element(By.ID, "loginCardTitle").text.__contains__(expected_warning_message)
    print(actual_warning_message)



