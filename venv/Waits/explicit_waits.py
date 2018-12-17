from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Chrome()
driver.get("https://www.expedia.com/Flights-Search?flight-type=on&starDate=12%2F06%2F2018&endDate=12%2F06%2F2018&mode=search&trip=roundtrip&leg1=from%3ASFO%2Cto%3ANYC%2Cdeparture%3A12%2F06%2F2018TANYT&leg2=from%3ANYC%2Cto%3ASFO%2Cdeparture%3A12%2F06%2F2018TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY")

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[NoSuchElementException,
                                         ElementNotVisibleException,
                                         ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH ,"//input[@id='stopFilter_stops-0']")))


element.click()

time.sleep(3)

driver.close()