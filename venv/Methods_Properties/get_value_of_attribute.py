# This is to find the value of the attribute of the element.

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.letskodeit.com/p/practice")

button = driver.find_element_by_xpath("//a[@id='opentab']")
attribute_value = button.get_attribute("class") #As argument we have provided the attribute name whose value we want


print(attribute_value)

time.sleep(3)

driver.close()