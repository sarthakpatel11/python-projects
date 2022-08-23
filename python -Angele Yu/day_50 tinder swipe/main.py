from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/zxc/Desktop/python/python -Angele Yu/devlopment/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")
span = driver.find_element_by_css_selector("span .keen-slider__slide")
span.click

driver.quit()
