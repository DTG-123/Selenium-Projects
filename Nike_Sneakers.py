from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.nike.com')

driver.find_element(By.XPATH, '//input[@name="search"]').send_keys("Men" + Keys.RETURN)
time.sleep(1)

items = driver.find_elements(By.XPATH, '(//a[@class="product-card__link-overlay"])[position() <6]')
prices = driver.find_elements(By.XPATH, '(//div[@data-testid="product-price"])[position() <6]')

for i, j in zip(items, prices):
    print(i.text, j.text, end="\n")

driver.quit()
