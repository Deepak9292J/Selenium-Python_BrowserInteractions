from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.letskodeit.com/p/practice")
driver.find_element_by_id("bmwradio").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@value='benz']").click()

print("The radio button for benz is {}".format(driver.find_element_by_xpath("//input[@value='benz']").is_selected()))

print("The radio button for benz is {}".format(driver.find_element_by_id("bmwradio").is_selected()))
driver.close()