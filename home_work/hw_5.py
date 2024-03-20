import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

icon_1= driver.find_element(By.CSS_SELECTOR, 'form > div:nth-child(1)')
icon_2= driver.find_element(By.CSS_SELECTOR, 'form > div:nth-child(2)')
icon_3= driver.find_element(By.CSS_SELECTOR, '#login-button')
if icon_1 and icon_2 and icon_3 is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')