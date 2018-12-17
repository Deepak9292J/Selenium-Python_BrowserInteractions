from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

email_input = driver.find_element_by_xpath("//input[@id='user_email']").send_keys("test@email.com")
password_input = driver.find_element_by_xpath("//input[@id='user_password']").send_keys("abcabc")
login_click = driver.find_element_by_xpath("//input[@value='Log In']").click()
all_courses = driver.find_element_by_xpath("//a[contains(text(),'All Courses')]").click()

#Write a dynamic xpath, using string format() function.
course_name = "//div[contains(@class,'course-listing-title') and contains(text(),'{}')]".format("Selenium WebDriver With Python 3.x")
driver.find_element_by_xpath(course_name).click()