from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.letskodeit.com/p/practice")

s = Select(driver.find_element_by_xpath("//select[@id='carselect']"))

# Select item by index
s.select_by_index(2)

time.sleep(2)

#Select item by visible text
s.select_by_value("benz")

time.sleep(2)

#Select item by value
s.select_by_visible_text("Honda")