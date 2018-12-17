from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")

button_text = driver.find_element_by_xpath("//a[@id='opentab']").text
print(button_text)

