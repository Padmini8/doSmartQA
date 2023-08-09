from behave import *
# from webdrivermanager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from behave import given, when, then
from selenium.webdriver.common.keys import Keys



# driver = None

@given('I launch the chrome browser')
def step_impl(context):
    # chrome_options = Options()
    # Options.add_argument("--no-proxy-server")
    # context.driver = webdriver.Chrome(options=chrome_options)
    # context.driver.maximize_window()
    context.driver = webdriver.Chrome()
    # time.sleep(5)

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


@then('User must successfully login to the project page')
def step_impl(context):
    driver = context.driver
    WebDriverWait(driver, 10).until(EC.url_contains('http://dosmartqa.stagsoftware.net:3009/main/projectselect'))
    # assert "Welcome to SmartQA" in driver.page_source
    # dashboard_element = context.driver.find_element_by_xpath('//*[@id="projectselectOpenExisting"]/a').text()
    # assert text=="Create Project"
    # context.driver.close
    # assert dashboard_element.is_displayed()

@then('I am on the dropdown page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    context.driver.get("http://dosmartqa.stagsoftware.net:3009/main/projectselect")
    time.sleep(5)

@then('I select option "{option}" from the dropdown')
def step_select_option_from_dropdown(context, option):
    dropdown_button = context.driver.find_element(By.XPATH, '//*[@id="openExisting"]/div[1]/div/div[1]/div/button')
    dropdown_button.click()
    option_xpath = f'//div[contains(@class, "dropdown-menu")]//span[text()="{option}"]'
    option_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchField"]')))
    time.sleep(3)
    option_element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="myProjectsList"]/tbody/tr/td')))
    option_element.click()


@then('Click on the Open project cta')
def step_click_open_project_cta(context):
    cta_button = context.driver.find_element(By.ID, 'projectselectExistOpen')
    context.driver.execute_script("arguments[0].scrollIntoView();", cta_button)
    cta_button.click()
    time.sleep(3)

@then('User successfully reached to dashboard')
def step_user_reached_dashboard(context):
    dashboard_title = "IstWs2"
    WebDriverWait(context.driver, 15).until(EC.title_contains(dashboard_title))
    time.sleep(5)

# @then('User successfully Logout')
# def step_select_option_from_dropdown(context, option):
#     dropdown_button = context.driver.find_element(By.XPATH, '//*[@id="hamburger"]/input').click()
#     time.sleep(5)
#     # dropdown_button.click()
#
#     # logout_button = context.driver.find_element(By.ID, 'logoutButton')
#     # logout_button.click()
    @then('User successfully Loggedout')
    def user_successful_logout(context):
        # Implementation of the step
        pass
