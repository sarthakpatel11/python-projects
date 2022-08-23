from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:/Learning Stuff/python/python -Angele Yu/devlopment/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.amazon.in/New-Apple-iPhone-Mini-128GB/dp/B08L5VG843/ref=sr_1_3?dchild=1&keywords=iphone+12+mini&qid=1626517754&sr=8-3")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# driver.quit()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# num = driver.find_element_by_css_selector("#articlecount a")
# print(num)
# num.click()
# driver.quit()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
driver.quit()
