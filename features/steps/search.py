from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I got navigated to Home page')
def step_impl(context):
   context.driver=webdriver.Chrome()
   context.driver.maximize_window()
   context.driver.get("https://tutorialsninja.com/demo/")


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")

@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//a[normalize-space()='HP LP3065']").is_displayed()
    context.driver.quit()


@when("I enter invalid product into the Search box field")
def enter_invalid_product(context):
    # Implement the code to enter an invalid product into the search box
    pass
    context.driver.find_element(By.NAME,"search").send_keys("Honda")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_text= "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)
    context.driver.quit()

@when("I dont enter anything into the Search box field")
def dont_enter_anything(context):
    # Implement the code to leave the search box empty
    pass
    context.driver.find_element(By.NAME,"search").send_keys("")
