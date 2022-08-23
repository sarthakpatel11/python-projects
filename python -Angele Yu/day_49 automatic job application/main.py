from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:/Learning Stuff/python/python -Angele Yu/devlopment/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    f"file:///C:/Users/zxc/Desktop/Sem%20-5%20All%20subject/WD/lab-6/lab-6.html")

email = driver.find_element_by_css_selector("#email")
repeateemail = driver.find_element_by_css_selector("#repeatemail")
password = driver.find_element_by_css_selector("#password")
repeatpassword = driver.find_element_by_css_selector("#repeatpassword")
submit = driver.find_element_by_css_selector("#submit")

email.send_keys("abc@abc.abc")
repeateemail.send_keys("abc@abc.abc")
password.send_keys("abc")
repeatpassword.send_keys("abc")
time.sleep(7)
submit.click()
time.sleep(5)

driver.quit()
