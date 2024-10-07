from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

pictures = WebDriverWait(driver, 40).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape")))

Src = driver.find_element(By.CSS_SELECTOR, "#landscape").get_attribute("src")

print(Src)

