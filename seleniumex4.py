from selenium import webdriver
driver=webdriver.(executable_path=r"C:\Users\HP\PycharmProjects\seleniumex3\driver\chromedriver.exe")
import time
driver.get("https://demo.actitime.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element_by_id("username").send_keys("admin")
driver.maximize_window()
time.sleep(4)
driver.find_element_by_name("pwd").send_keys("manager")
time.sleep(4)
driver.find_elements_by_id("loginButtonContainer").click()