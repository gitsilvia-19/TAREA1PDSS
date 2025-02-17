from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
elem = driver.find_element_by_id("email")
elem.clear()
elem.send_keys("salex_lara@hotmail.com")

elem = driver.find_element_by_id("pass")
elem.clear()
elem.send_keys("")

elem.send_keys(Keys.RETURN)
