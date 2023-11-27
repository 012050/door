import os
import dotenv
from flask import Flask, jsonify, request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
# 아이디, 비밀번호 환경변수에서 가져오기
dotenv.load_dotenv(dotenv.find_dotenv())
ID = os.environ["ID"]
PW = os.environ["PW"]

app = Flask(__name__)

@app.route("/")
def EspDataReturn():
    # path = os.getcwd() + "\chromedriver.exe"
    # driver = webdriver.Chrome(path)
    
    # driver.get("https://door.deu.ac.kr/sso/login.aspx")
    # driver.implicitly_wait(60)
    # login = driver.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")
    # login.send_keys(ID, Keys.TAB, PW, Keys.RETURN)
    # driver.implicitly_wait(60)
    # driver.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
    # driver.implicitly_wait(60)
    # driver.find_element(By.ID, "btn_quick_close").click()
    # driver.implicitly_wait(10)
    # print("프로그램 종료")
    # time.sleep(10)
    # driver.close()
    json_data = {
        "subject": ["자바 프로그래밍", "비주얼 프로그래밍", "자료구조", "컴퓨터구조"],
        "1" : "[수업활동일지] 2주차 언어구조 9.8",
        "2" : "[수업활동일지] 실습파일파일제출(2) 9.19",
        "3" : "[수업활동일지] 실습파일파일제출(3) 9.26",
        "4" : "[수업활동일지] 실습파일파일제출(4) 10.10",
        "5" : "[수업활동일지] 10.17 실습파일파일제출(5)",
        "6" : "[수업활동일지] 10.24 실습파일파일제출(7)",
        "7" : "[수업활동일지] 실습파일파일제출(8) 11.37",
        "8" : "[수업활동일지] 8장 컨트롤 / 10장 고급폼 11.14",
        "9" : "[수업활동일지] 파일입출력 11.21",
        }
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)