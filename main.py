#웹 실행
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#요소를 찾기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#경로 확인
import os

# 프로그램 종료
import sys

#옵션
import argparse

import time

def door_login(name):
    name.get("https://door.deu.ac.kr/sso/login.aspx")
    name.implicitly_wait(60)
    login = name.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")
    login.send_keys(s_id)
    pw = name.find_element(By.CLASS_NAME,"i_text")
    pw.send_keys(s_pw,Keys.RETURN)
    name.implicitly_wait(60)
    name.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
    # b12 = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(By.XPATH, '//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a'))
    # b12.click()
    name.implicitly_wait(60)
    name.find_element(By.ID, "btn_quick_close").click()
    name.implicitly_wait(10)
def dorm_login(name):
    # name.get("https://dorm.deu.ac.kr/deu")
    name.get("https://dorm.deu.ac.kr/deu/00/0000.kmc#")
    name.implicitly_wait(60)
    name.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[5]/a").click()
    name.implicitly_wait(60)
    a = name.find_elements(By.CLASS_NAME, "in_idpw")[0]
    a.send_keys(s_id, Keys.TAB, s_pw, Keys.RETURN)
    name.implicitly_wait(60)
    b = name.find_element(By.XPATH, "/html/body/div/div/div[3]/div/ul[2]/li/span[2]/a")
    b.click()
    name.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")
def page_close(name):
    print("추가 팝업창은 다음과 같습니다.", name.window_handles)
    try:
        main = name.window_handles
        for handle in main:
            if handle != main[0]:
                # print(main[handle])
                name.switch_to.window(handle)
                name.close()
        name.switch_to.window(main[0])
    except:
        print("\n오류가 발생했습니다.\n")

# -------------------------------------------
# 시작 페이지 설정(기본: door)
parser = argparse.ArgumentParser()
parser.add_argument('--page', type=str, default='door', help='Set start page')
args = parser.parse_args()

# 텍스트 파일에서 아이디, 비밀번호 가져오기
try:
    path1 = os.getcwd() + "\personal_info.txt"
    f = open(path1, "r")
    info_data = f.read()
    f.close()
    s_id = info_data.split("\n")[0]
    s_pw = info_data.split("\n")[1]
except:
    print("Please enter your ID and password")
    s_id = input("ID: ")
    s_pw = input("PASSWORD: ")
    p_file = open("personal_info.txt", "w")
    p_file.write(s_id + "\n" + s_pw)
    p_file.close()

# 크롬드라이버 찾기
path2 = os.getcwd() + "\chromedriver.exe"
driver = webdriver.Chrome(path2)

# 창 크기 조절
# driver.maximize_window()
mm = driver.get_window_size()
print(mm.get("width"), mm.get("height"))
driver.set_window_size(984, 945)


check = "door"
dorm = 0
door_login(driver)

a = args.page

try:
    while 1:
        if a == "stop" or a == "exit":
            driver.close()
            sys.exit("\n프로그램을 종료합니다.\n")

        elif a == "size":
            size = driver.get_window_size()
            w = size.get("width")
            h = size.get("height")
            print(w, h)
    # -------------------------------------------
    # 팝업 창 닫기
        elif a == "close":
            page_close(driver)
    # -------------------------------------------
    # 화면최대화
        elif a == "full":
            driver.maximize_window()

    # -------------------------------------------
    # 도어, 기숙사 페이지 전환
        elif a == "door":
            if check == "door":
                print("Already we are door page")
            else:
                driver.get("http://door.deu.ac.kr/MyPage")
                check = "door"

        elif a == "dorm":
            if check == "dorm":
                print("Already we are dorm page")
            
            elif a == "dorm" and dorm == 0:
                dorm_login(driver)
                print("\ndorm\n")
                check = "dorm"
                dorm = 1
                
            elif a == "dorm" and dorm == 1:
                driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")

        elif a == "search":
            check = "search"
            driver.get("http://door.deu.ac.kr/Community/MessageSend")
            driver.implicitly_wait(60)
            driver.find_element(By.CSS_SELECTOR, "#popsearch > span > button").click()
            driver.get("http://door.deu.ac.kr/MyPage")
    # -------------------------------------------
    #도어, 기숙사 페이지 내부 이동
        elif (a == "main") and check == "door":
            driver.get("http://door.deu.ac.kr/MyPage")

        elif (a == "re" or a == "login") and check == "door":
            door_login(driver)

        elif (a == "main") and check == "dorm":
            driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")
            
        elif (a == "out"):
            if dorm == 0:
                dorm_login(driver)
            check = "dorm"
            driver.get("https://dorm.deu.ac.kr/deu/stayout/getStayoutWriteView.kmc?seq=&stayout_locgbn=DE&list_type=mypage")
    # -------------------------------------------
    #네이버 맞춤법 검사기
        elif a == "naver":
            driver.get("https://search.naver.com/search.naver?ie=UTF-8&query=%EB%9D%84%EC%96%B4%EC%93%B0%EA%B8%B0+%EA%B2%80%EC%82%AC%EA%B8%B0&sm=chr_hty")
            check = "naver"
            count = 0
            while 1:
                b = str(input("맞춤법 검사기 - 맞춤법 검사를 원하는 단어나 문장을 입력해 주세요.\n>>"))
                if b == "stop" or b == "exit" or b == "정지" or b == "멈춤":
                    break
                driver.find_elements(By.CLASS_NAME, "text_area")[0].click()

    # -------------------------------------------
    # 학사 일정
        elif a == "home" or a == "deu":
            driver.get("https://www.deu.ac.kr/www/academic_calendar")
            driver.implicitly_wait(60)
            check = "home"

    # -------------------------------------------
        elif a == "dap":
            driver.get("https://dap.deu.ac.kr/sso/login.aspx")
            driver.implicitly_wait(60)
            dap_id = driver.find_element(By.XPATH, "/html/body/form/div[1]/div/div[1]/div[2]/input")
            dap_pw = driver.find_element(By.XPATH, "/html/body/form/div[1]/div/div[1]/div[3]/input") 
            dap_id.send_keys(s_id)
            dap_pw.send_keys(s_pw, Keys.RETURN)
            driver.implicitly_wait(60)
            time.sleep(1)
            check = "dap"
        a = input('\n\nif you want to stop, press ctrl + c or input "stop"\n:')
        a = a.lower()
        print(a)
except:
    print("\n에러가 발생했습니다.\n")
    driver.close()
    sys.exit()