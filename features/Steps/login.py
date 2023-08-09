from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigated to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,"Login").click()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("amotooriapril2023@gmail.com")
    context.driver.find_element(By.ID,"input-password").send_keys("12345")


@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    print("Inside - I should get logged in")


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    print("Inside - I enter invalid email and valid password into the fields")


@then(u'I should get a proper warning message')
def step_impl(context):
    print("Inside - I should get a proper warning message")


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter valid email and invalid password into the fields")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    print("Inside - I enter invalid email and invalid password into the fields")


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    print("Inside - I dont enter anything into email and password fields")