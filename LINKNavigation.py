from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# You can only use the LINK locators to navigate to anchor tags (<a>)
# LINK_TEXT is for full link, PARTIAL_LINK_TEXT is for text in the link that will not change
# CLASS_NAME can also be used to detect the link here
driver.find_element(By.PARTIAL_LINK_TEXT, 'Free Access').click()
time.sleep(2)
driver.back()

time.sleep(2)
driver.quit()
