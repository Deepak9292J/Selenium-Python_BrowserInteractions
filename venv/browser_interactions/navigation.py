from selenium import  webdriver

driver = webdriver.Chrome()

#Enter the page URL
driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

#Maximise window
driver.maximize_window()

#Get current page title
driver.title

#Refresh the page
driver.refresh()

#Get current page source
print(driver.page_source)

driver.get("https://www.google.com/")

#Go back to previous page
driver.back()

#Move forward by one page
driver.forward()

#Close current instance of browser.
driver.close()


