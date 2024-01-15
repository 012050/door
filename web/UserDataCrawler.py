
import time
import json
import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

selection_option_index = 1

def GetUserData(ID, PW):
    json_data = {}

    driver = webdriver.Chrome("chromedriver")

    Login(driver, ID, PW)

    # 학기 설정(테스트용)
    tno = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/select')
    spin_options = Select(tno)
    # 1학기 전을 선택(2023 2학기)
    spin_options.select_by_index(selection_option_index)

    # 강의실 목록
    lecture_list = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[2]/div[3]/div[3]/table/tbody/tr')
    lecture_list.pop(0)
    for lecture_number in range(len(lecture_list)):
        # 학기 설정(테스트용)
        tno = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/select')
        spin_options = Select(tno)
        spin_options.select_by_index(selection_option_index)

        lecture_click_list = f"/html/body/div[2]/div[2]/div[3]/div[3]/table/tbody/tr[{int(lecture_number) + 2}]/td[3]/a"
        lecture_list_name = driver.find_element(By.XPATH, lecture_click_list)
        lecture_name = lecture_list_name.text
        json_data[lecture_name] = {}
        lecture_list_name.click()
        time.sleep(2)
        # 과제 확인 코드
        GetTaskData(driver, json_data, lecture_name)
        # 수업활동일지 확인 코드
        GetJournalData(driver, json_data, lecture_name)

        # 강의실로 돌아가기
        driver.get("http://door.deu.ac.kr/MyPage")
        driver.implicitly_wait(10)

    print("프로그램 종료")
    driver.close()
    file_name = f"{ID}.json"
    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    return 0

def Login(driver, ID, PW):
    driver.get("http://door.deu.ac.kr/sso/login.aspx")
    driver.implicitly_wait(60)
    login = driver.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")
    login.send_keys(ID, Keys.TAB, PW, Keys.RETURN)
    driver.implicitly_wait(60)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "btn_quick_close").click()
    driver.implicitly_wait(10)
    return 0

def GetTaskData(driver, json_data, lecture_name):
    try:
        print(f"과제 확인 코드 : {lecture_name}")
        # 과제 버튼 클릭
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/ul/li/ul/li[3]/a/span").click()
        driver.implicitly_wait(10)
        task_list = driver.find_elements(By.XPATH, '//*[@id="sub_content2"]/div/table/tbody/tr')
        task_list.pop(0)
        json_data[lecture_name]['task'] = []
        if(task_list[0].text != "등록된 과제가 없습니다."):
            for task_number in range(len(task_list)):
                driver.find_element(By.XPATH, f'//*[@id="sub_content2"]/div/table/tbody/tr[{task_number + 2}]/td[3]/a').click()
                print(f"{task_number + 1}번째 과제 확인")
                period = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[2]/td[1]').text
                title = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[3]/td').text
                content = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[4]/td').text
                print(lecture_name)
                # json_data[lecture_name].append({ "task" : {"period" : period, "title" : title, "content" : content}})
                json_data[lecture_name]['task'].append({"period" : period, "title" : title, "content" : content})
                driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/ul/li/ul/li[3]/a/span").click()
                driver.implicitly_wait(10)
        else:
            print("else문")
            print(task_list[0].text)
            json_data[lecture_name]['task'] = None
    except:
        print(f"과제 확인 오류 : {lecture_name}")
    return 0

def GetJournalData(driver, json_data, lecture_name):
    try:
        print("수업활동일지 확인 코드")
        driver.find_element(By.XPATH, '//*[@id="lnbContent"]/div/div[4]/ul/li/ul/li[1]/a/span').click()
        driver.implicitly_wait(10)
        lecture_journal = driver.find_elements(By.XPATH, '//*[@id="sub_content2"]/div/table/tbody/tr')
        lecture_journal.pop(0)
        for i in lecture_journal:
            print(i.text)
        json_data[lecture_name]['journal'] = []
        if(lecture_journal[0].text != "등록된 산출물이 없습니다."):
            for journal_number in range(len(lecture_journal)):
                driver.find_element(By.XPATH,  f'//*[@id="sub_content2"]/div/table/tbody/tr[{journal_number + 2}]/td[2]/a').click()
                period = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[2]/td[1]').text
                title = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[3]/td').text
                content = driver.find_element(By.XPATH, '//*[@id="sub_content2"]/div[1]/table/tbody/tr[4]/td').text
                print(lecture_name)
                json_data[lecture_name]['journal'].append({"period" : period, "title" : title, "content" : content})
                driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/ul/li/ul/li[3]/a/span").click()
                driver.implicitly_wait(10)
        else:
            print("else문")
            print(lecture_journal[0].text)
            json_data[lecture_name]['journal'] = None

    except:
        print(f"수업활동일지 확인 오류 : {lecture_name}")
    return 0

if __name__ == "__main__":
    import os
    import dotenv
    start_time = time.time()
    dotenv.load_dotenv(dotenv.find_dotenv())
    id = os.environ["ID"]
    pw = os.environ["PW"]

    GetUserData(ID=id, PW=pw)
    
    print("--- %s seconds ---" % (time.time() - start_time))
