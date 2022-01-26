from selenium import webdriver
driver =webdriver.Chrome(executable_path=r"C:\Users\HP\PycharmProjects\seleniumex3\driver.exe")
from selenium.webdriver.common.keys
import keys
import time
driver.get("https://demoweb.actitime.com/login.do")
time sleep(2)
username=driver.find_element_by_css_selector('input ([id ="username"]')
