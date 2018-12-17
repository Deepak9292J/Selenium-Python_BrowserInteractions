from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.expedia.com/")

section_under_test = driver.find_element_by_xpath("//div[@class='gcw-advanced-options-wrapper']")
flight_car = driver.find_element_by_xpath("//input[@id='fc-fc-hp-package']")
flight_hotel = driver.find_element_by_xpath("//input[@id='fh-fh-hp-package']")

#Check if the section under test is displayed or not.
print("Inititally, the section display status is {}".format(section_under_test.is_displayed()))

#Select flight+Car option
flight_car.click()

#Check if the section under test is displayed or not.
print("After select flight+Car, the section display status is {}".format(section_under_test.is_displayed()))

