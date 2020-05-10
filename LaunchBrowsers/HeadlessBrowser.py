import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "D:\\Testing Purpose\\Pycharm Testing\\selenium_with_python\\Python_basics\\Drivers\\chromedriver.exe "
 

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory


# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")

driver.close()


 

