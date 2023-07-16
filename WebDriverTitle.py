from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.nike.com")
driver.maximize_window()

assert "Nike" in driver.title
# This is an assertion to see if "Nike" is there in the title of the website
print(driver.title)

driver.quit()
