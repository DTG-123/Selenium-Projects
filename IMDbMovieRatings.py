from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

movie = input("\033[1;32mWhich movie's rating would you like to see?" + "\n" + "- ")

driver = webdriver.Chrome()
driver.get('https://www.imdb.com')

search_bar = driver.find_element(By.XPATH, '//input[@type="text"]')
search_bar.send_keys(str(movie))
search_bar.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//li[@class="ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result"]').click()

movie_name = driver.find_element(By.XPATH, '//span[@class="sc-afe43def-1 fDTGTb"]')
rating = driver.find_element(By.XPATH, '//span[@class="sc-bde20123-1 iZlgcd"]')
print("\033[33m" + "IMDb rating of " + movie_name.text + " - " + rating.text + "/10")

actors = driver.find_elements(By.CSS_SELECTOR, 'a[class="sc-bfec09a1-1 fUguci"]')
x = 1
print("\033[1;36mThe actors in this film are - ")
for list in actors:
    print(str(x) + ")" + list.text, end="\n")
    x += 1
driver.quit()
