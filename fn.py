
# def door_login(name):
#     name.get("https://door.deu.ac.kr/sso/login.aspx")
#     name.implicitly_wait(60)
#     login = name.find_element(By.XPATH,"/html/body/form/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input")
#     login.send_keys(s_id)
#     pw = name.find_element(By.CLASS_NAME,"i_text")
#     pw.send_keys(s_pw,Keys.RETURN)
#     name.implicitly_wait(60)
#     name.find_element(By.XPATH,'//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a').click()
#     # b12 = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located(By.XPATH, '//*[@id="gnbContent"]/div/div[2]/ol[2]/li[3]/a'))
#     # b12.click()
#     name.implicitly_wait(60)
#     name.find_element(By.ID, "btn_quick_close").click()
#     name.implicitly_wait(10)
# def dorm_login(name):
#     # name.get("https://dorm.deu.ac.kr/deu")
#     name.get("https://dorm.deu.ac.kr/deu/00/0000.kmc#")
#     name.implicitly_wait(60)
#     name.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[5]/a").click()
#     name.implicitly_wait(60)
#     a = name.find_elements(By.CLASS_NAME, "in_idpw")[0]
#     a.send_keys(s_id, Keys.TAB, s_pw, Keys.RETURN)
#     name.implicitly_wait(60)
#     b = name.find_element(By.XPATH, "/html/body/div/div/div[3]/div/ul[2]/li/span[2]/a")
#     b.click()
#     name.get("https://dorm.deu.ac.kr/deu/50/5050.kmc")
# def page_close(name):
#     print("추가 팝업창은 다음과 같습니다.", name.window_handles)
#     try:
#         main = name.window_handles
#         for handle in main:
#             if handle != main[0]:
#                 name.switch_to.window(handle)
#                 name.close()
#     except:
#         print("\n오류가 발생했습니다.\n")
