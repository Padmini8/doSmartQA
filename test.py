from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.NAME, "email").send_keys("Pamini_123.io")
driver.find_element(By.NAME,"pass").send_keys("Pamini_123.io")
driver.find_element(By.NAME,"login").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(href,'login/identify'])"))
    )
    print("test passed")
except:
    print("test failed")

