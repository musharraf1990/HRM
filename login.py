from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
PATH= Service ("D:\Musharraf\Selenium Automation\Care Modules\chromedriver.exe")
driver = webdriver.Chrome(service=PATH, options=chrome_options)

def Login():
    driver.get("http://172.16.10.4:8082/jw/web/login")
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.ID,"j_username").send_keys("admin")
    driver.find_element(By.ID, "j_password").send_keys("CareKamra@2022")
    driver.find_element(By.NAME,"submit").click()
    sleep(2)