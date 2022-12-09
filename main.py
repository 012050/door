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
    driver.find_element(By.ID, "btn_quick_close").click()
    driver.implicitly_wait(10)

def dorm_login():
    # driver.get("https://dorm.deu.ac.kr/deu")
    driver.get("https://dorm.deu.ac.kr/deu/00/0000.kmc#")
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[5]/a").click()
    driver.implicitly_wait(60)
    a = driver.find_elements(By.CLASS_NAME, "in_idpw")[0]
    a.send_keys(s_id, Keys.TAB, s_pw, Keys.RETURN)
    driver.implicitly_wait(60)
    b = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/ul[2]/li/span[2]/a")
    b.click()
    driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")


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

# 창 크기 조절
# driver.maximize_window()
mm = driver.get_window_size()
print(mm.get("width"), mm.get("height"))
driver.set_window_size(984, 945)


check = "door"
dorm = 0

try:
    door_login()

except:
    door_login()


try:
    while 1:
        a = input('\n\nif you want to stop, press ctrl + c or input "stop"\n:')

        if a == "stop" or a == "exit":
            driver.close()
            os._exit(1)
        elif a == "size":
            size = driver.get_window_size()
            w = size.get("width")
            h = size.get("height")
            print(w, h)
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
                dorm_login()
                print("\ndorm\n")
                check = "dorm"
                dorm = 1
                
            elif a == "dorm" and dorm == 1:
                driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")
        
        elif a == "search":
            check = "search"
            driver.get("http://door.deu.ac.kr/Community/MessageSend")
            # driver.get("http://door.deu.ac.kr/Community/PopUserList?type=none&searchtype=name&searchvaleu=")
            driver.implicitly_wait(60)
            driver.find_element(By.CSS_SELECTOR, "#popsearch > span > button").click()
            driver.get("http://door.deu.ac.kr/MyPage")
            # bbb = driver.find_element(By.CLASS_NAME, "i_text")
            # while 1:
            #     bc = input()
            #     if bc == "exit" or bc == "stop" or bc == "멈춤":
            #         break
            #     bbb.send_keys(bc, Keys.RETURN)

    # -------------------------------------------
    #도어, 기숙사 페이지 내부 이동
        elif (a == "main") and check == "door":
            driver.get("http://door.deu.ac.kr/MyPage")

        elif (a == "re" or a == "login") and check == "door":
            door_login()

        elif (a == "main") and check == "dorm":
            driver.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")
            
        elif (a == "out"):
            if dorm == 0:
                dorm_login()
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
                
                # driver.implicitly_wait(60)
                # driver.find_element(By.CLASS_NAME, "delete_btn").click()
                driver.find_elements(By.CLASS_NAME, "text_area")[0].click()
                # ff = driver.find_element(By.CLASS_NAME, "txt_gray")
                # ff.send_keys("안녕하세요", Keys.RETURN)

except:
    driver.get("http://door.deu.ac.kr/MyPage")
os._exit(1)