#웹 실행
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#요소를 찾기
from selenium.webdriver.common.by import By

#경로 확인
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

def dorm():
    # driver.get("https://dorm.deu.ac.kr/")
    driver.get("https://dorm.deu.ac.kr/deu")
    driver.implicitly_wait(60)
    # a = driver.find_elements(By.CLASS_NAME, "login")[10]
    # a.click()

# 텍스트 파일에서 아이디, 비밀번호 가져오기
path1 = os.getcwd() + "\personal_info.txt"
f = open(path1, "r")
info_data = f.read()
f.close()
s_id = info_data.split("\n")[0]
s_pw = info_data.split("\n")[1]

# 크롬드라이버 찾기
path2 = os.getcwd() + "\chromedriver.exe"
driver = webdriver.Chrome(path2)

# 창 최대화
driver.maximize_window()


check = "door"

door_login()

while 1:
    a = input('\n\nif you want to stop, press ctrl + c or input "stop"\n:')

    if a == "stop" or a == "exit":
        driver.close()
        os._exit(1)

    elif a == "dorm":
        dorm()
        check = "dorm"

    elif a == "main" and check == "door":
        driver.get("http://door.deu.ac.kr/MyPage")

    elif a ==  "main" and check == "dorm":
        driver.get("https://dorm.deu.ac.kr/")

    elif a == "re" or a == "login":
        door_login()
    

os._exit(1)