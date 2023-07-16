import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

href = driver.find_element(By.CLASS_NAME, "blinkingText")
print(href.get_attribute("href"))
time.sleep(1)

driver.get('https://nike.com')
links = driver.find_elements(By.XPATH, '//li[@slidecount="10"]//div//a')
for link in links:
    print(link.get_attribute("href"))

driver.quit()