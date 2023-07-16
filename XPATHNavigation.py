from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


# Format for XPATH:
# 1 Attribute and Value - //tagname[@attribute = "value"]
# 2 Attributes and Value - //tagname[@attribute1 = "value1" and/or @attribute2 = "value2" and/or ...]
driver.find_element(By.XPATH, '//input[@value="radio3" and @name="radioButton"]').click()

# Text (If what you're locating is in an attribute-less tag, e.g. - <strong>DG</strong>) - //tagname[text() = "text"]
driver.find_element(By.XPATH, '//legend[text() = "Radio Button Example"]')

# Using Parents - //grandparent_tagname[@grandparent_attribute = "value"]/parent_tagname//tagname[@attribute = "value"]
time.sleep(3)
driver.find_element(By.XPATH, '//div[@id="radio-btn-example"]/fieldset/label[@for="radio1"]/input').click()

# Using Children - //child_tagname[@attribute = "value"]/ancestor::parent_tagname[...]  
driver.find_element(By.XPATH, '//input[@value="option1"]/ancestor::label')

# If there are multiple tags, but you want to access a certain one by number - (//tagname[...])[x]
# If there are multiple tags, but you want to access certain ones by number - (//tagname[...])[position()<x or >x]
# This accesses only the number of tags you have specified, for example if you want to access only 6 tags, (//tagname[...])[position()<7]
# If the last one is wanted - (//tagname[...])[last()]
time.sleep(3)
driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '(//input[@type="checkbox"])[last()]').click()

# NOTE - Instead of //tagname, //* can be used. It will detect all tags with the attributes given

time.sleep(3)
driver.quit()