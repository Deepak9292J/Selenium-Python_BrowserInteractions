from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://www.google.com/"
driver.get(base_url)

search_box =  driver.find_element_by_xpath("//input[@title='Search']")
search_box.send_keys("test")
print("The state of the button is: {} ".format(search_box.is_enabled()))
driver.close()
