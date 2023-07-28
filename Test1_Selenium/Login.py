import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# First commit
#Changes by Padmini
#Changes by Develop
#new changes

driver = webdriver.Chrome()
driver.get('http://dosmartqa.stagsoftware.net:3009/login')

driver.find_element(By.NAME,"email").send_keys("Padmini")
time.sleep(4)
driver.find_element(By.ID,"password").send_keys("Micky@098")
time.sleep(4)
driver.find_element(By.CLASS_NAME,"form-submit-button").click()
time.sleep(4)
driver.find_element(By.ID,"projectselectExistOpen").click()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(4)