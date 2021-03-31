import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

CHROME_PATH = "/home/thekillingjoke/Music/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_PATH)
driver.get(
    url="https://www.linkedin.com/jobs/search/?currentJobId=2454286091&f_AL=true&geoId=102713980&keywords=python%20developer&location=India")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys("Email")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Password")
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("Number")

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()