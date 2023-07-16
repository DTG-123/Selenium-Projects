from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
check_boxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

print(len(check_boxes))

for x in check_boxes:
    x.click()
    print(x)
    time.sleep(1)

time.sleep(2)
driver.quit()