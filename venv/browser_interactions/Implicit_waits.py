from  selenium import webdriver
import time

driver = webdriver.Chrome()

#Provide implicit wait in this manner
driver.implicitly_wait(10)

#Enter the page URL
driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

email_field = driver.find_element_by_id("user_email")

password_field = driver.find_element_by_id("user_password")

login_button = driver.find_element_by_xpath("//input[@type='submit']")

email_field.send_keys("test")
password_field.send_keys("pass")
time.sleep(3)
email_field.clear()
time.sleep(3)
email_field.send_keys("test2")
login_button.click()
time.sleep(3)

#Close current instance of browser
driver.close()
