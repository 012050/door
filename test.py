
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

path1 = os.getcwd() + "\personal_info.txt"
f = open(path1, "r")
info_data = f.read()
f.close()
s_id = info_data.split("\n")[0]
s_pw = info_data.split("\n")[1]
path2 = os.getcwd() + "\chromedriver.exe"
driver = webdriver.Chrome(path2)

driver.maximize_window()


driver.get("https://dorm.deu.ac.kr/deu/00/0000.kmc#")
driver.implicitly_wait(60)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[5]/a").click()
driver.implicitly_wait(60)
a = driver.find_elements(By.CLASS_NAME, "in_idpw")[0]
a.send_keys(s_id, Keys.TAB, s_pw, Keys.RETURN)
driver.implicitly_wait(60)
b = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/ul[2]/li/span[2]/a")
b.click()
# driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")