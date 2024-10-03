from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/dynamicid")


Add_Elements = driver.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
sleep(1)
