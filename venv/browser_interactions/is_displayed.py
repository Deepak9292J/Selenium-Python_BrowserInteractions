from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.letskodeit.com/p/practice")

hide_button = driver.find_element_by_xpath("//input[@id='hide-textbox']")
show_button = driver.find_element_by_xpath("//input[@id='show-textbox']")
input_box = driver.find_element_by_xpath("//input[@id='displayed-text']")

#Check whether the input box is currently displayed or not.
print("Initially, the field display status is {}".format(input_box.is_displayed()))

#Click Hide Button
hide_button.click()

#Check whether the input box is currently displayed or not.
print("After Hide button click, the field display status is {}".format(input_box.is_displayed()))

time.sleep(3)

#Click Show Button
show_button.click()

#Check whether the input box is currently displayed or not.
print("After clicking show button, the field display status is {}".format(input_box.is_displayed()))

#Close the browser
driver.close()