from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = (
    "D:/Learning Stuff/python/python -Angele Yu/devlopment/chromedriver.exe"
)
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
URL = "https://web.telegram.org/k/"
NUMBER = "number"
driver.get(URL)
time.sleep(10)
phone_button = driver.find_element_by_css_selector("div .c-ripple")
phone_button.click()
time.sleep(5)
phone_number = driver.find_element_by_name("phone")
phone_number.send_keys(NUMBER)
time.sleep(5)
next_button = driver.find_element_by_css_selector(".btn-color-primary")
next_button.click()
time.sleep(30)

search_input = driver.find_element_by_css_selector(".input-search-input")
search_input.send_keys("Saved Messages")
time.sleep(5)
search_input = driver.find_element_by_xpath(
    '//*[@id="search-container"]/div[2]/div/div/div[1]/div/div[1]/ul/li/div[1]'
)
search_input.click()
input_message = driver.find_element_by_css_selector(".input-message-input")
input_message.send_keys("Hi Just trying Pythone Bot.")
input_message.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
