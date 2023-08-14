from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('user input wrong credentials')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")
    context.driver.find_element(By.NAME, "email").send_keys("Pamini_123.io")
    context.driver.find_element(By.NAME, "pass").send_keys("Pamini_123.io")
    context.driver.find_element(By.NAME, "login").click()

@then('Error message will come')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(href,'login/identify'])"))
        )
        print("test passed")
    except:
        print("test failed")



