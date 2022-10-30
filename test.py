
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


def door_login():
    driver.get("https://door.deu.ac.kr/sso/login.aspx")
    driver.implicitly_wait(60)
    login = driver.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")
    login.send_keys(s_id)
    pw = driver.find_element(By.CLASS_NAME,"i_text")
    pw.send_keys(s_pw,Keys.RETURN)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
    driver.implicitly_wait(60)


path1 = os.getcwd() + "\personal_info.txt"
f = open(path1, "r")
info_data = f.read()
f.close()
s_id = info_data.split("\n")[0]
s_pw = info_data.split("\n")[1]
path2 = os.getcwd() + "\chromedriver.exe"
driver = webdriver.Chrome(path2)

door_login()


for a in range(1, 5):
    print(a)
    time.sleep(1)
driver.close()