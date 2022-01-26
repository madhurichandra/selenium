from selenium import webdriver
driver =webdriver.Chrome(executable_path=r"C:\Users\HP\PycharmProjects\seleniumex3\driver\chromedriver.exe")
import time
driver.get("http://demowebshop.tricentis.com/")
time.sleep(4)
driver.find_element_by_class_name("ico-register").click()
driver.find_element_by_link_text("Books").click()
time.sleep(2)
driver.find_element_by_link_text("Computers").click()
time.sleep(2)
driver.find_element_by_link_text("Electronics").click()
time.sleep(2)
driver.find_element_by_link_text("Apparel & Shoes").click()
time.sleep(2)
driver.find_element_by_link_text("Digital downloads").click()
time.sleep(2)
driver.find_element_by_link_text("Jewelry").click()
time.sleep(2)
driver.find_element_by_link_text("Gift Cards").click()
time.sleep(2)

driver.find_element_by_id("small-searchterms").send_keys("Books")
driver.find_element_by_css_selector('input[class="button-1 search-box-button"]').click()
time.sleep(2)
driver.find_element_by_id("small-searchterms").send_keys("Computers")
driver.find_element_by_css_selector('input[class="button-1 search-box-button"]').click()


time.sleep(2)


