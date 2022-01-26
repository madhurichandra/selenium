from selenium import webdriver
driver =webdriver.Chrome(executable_path=r"C:\Users\HP\PycharmProjects\seleniumex3\driver\chromedriver.exe")
import time
driver.get("http://demo.actitime.com/")
time.sleep(4)
driver.find_element_by_css_selector('input[placeholder="Username"]').send_keys("admin")
time.sleep(2)
driver.find_element_by_css_selector('input[placeholder="Password"]').send_keys("manager")
time.sleep(2)
driver.find_element_by_css_selector('a[id="loginButton"]').click()