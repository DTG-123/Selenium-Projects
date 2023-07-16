from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

static_dropdown = driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]')
select = Select(static_dropdown)
select.select_by_index(1)
time.sleep(1)
select.select_by_visible_text("Option2")
time.sleep(1)
select.select_by_value("option3")
time.sleep(1)

# You can also directly access the dropdown option
option = driver.find_element(By.XPATH, '//option[@value="option2"]')
option.click()
print(option.text)

time.sleep(1)
driver.quit()