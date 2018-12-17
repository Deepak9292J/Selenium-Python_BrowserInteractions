from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.letskodeit.com/p/practice")

number_of_checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print("The number of checkboxes are {}".format(len(number_of_checkboxes)))

for checkbox in number_of_checkboxes:
    checkbox.click()
    time.sleep(2)
