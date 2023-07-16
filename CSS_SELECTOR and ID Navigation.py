from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.ID, 'checkBoxOption3').click()

# CSS_SELECTOR can be found with:
# CLASS - tagname.classvalue
# ID - tagname#IDvalue
# Attribute and value - tagname[attribute = 'value']
# If they are still common with the other tags, we can use - tagname.classvalue[attribute='value]
# NOTE - The tagname is not necessary if the tag is unique
driver.find_element(By.CSS_SELECTOR, 'input[value="radio2"]').click()


driver.find_element(By.CSS_SELECTOR, 'input.inputs[id="name"]').send_keys("DG")

time.sleep(2)
driver.quit()
