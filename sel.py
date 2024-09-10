from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import pyautogui

urls = [

    'https://translate.google.com/?sl=auto&tl=hi&op=translate' 
      ]
s = Service(r"/usr/bin/chromedriver")
import time
for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(2)

    click_button=driver.find_element(by=By.XPATH, value="//span[normalize-space()='Images']")

    click_button.click()
    time.sleep(2)
    click_button1=driver.find_element(by=By.XPATH, value="//label[@for='ucj-39']")
    click_button1.click()
    print(1)
    time.sleep(8)

    pyautogui.doubleClick(612,166, duration=3)
    print(2)
    #click_button1.send_keys(r'/home/mani/Downloads/Tantraraja Tantra by Avalon Lakshamana Shastri  - Jangamwadi Math Collection_0109 (2) (1).jpg')
    #click_button1.send_keys(os.getcwd() + "/home/mani/Downloads/Tantraraja Tantra by Avalon Lakshamana Shastri  - Jangamwadi Math Collection_0109 (2) (1).jpg")
    time.sleep(8)

    click_button2=driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[5]/c-wiz/div[2]/c-wiz/div/div[1]/div[2]/div[2]/button/span[1]/svg")
    click_button2.click()
    print(4)
    time.sleep(20)
