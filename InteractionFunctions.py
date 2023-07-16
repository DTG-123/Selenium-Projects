from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# The interaction functions for input fields are: .sendkeys() - types,
#                                                .click() - clicks,
#                                                .clear() - clears input field,
#                                                .text - copies text

input_field = driver.find_element(By.XPATH, '//input[@id="name"]')
input_field.send_keys("DG")
time.sleep(2)
input_field.clear()
time.sleep(2)
input_field.send_keys("Dhruv G")
time.sleep(2)

alert_example = driver.find_element(By.XPATH, '//fieldset[@class="pull-right"]/legend')
print(alert_example.text)
time.sleep(2)

dropdown = Select(driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]'))
dropdown.select_by_index(2)
time.sleep(2)

driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()

time.sleep(2)
driver.quit()
