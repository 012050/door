import os
import cryptography

try:
    path1 = os.getcwd() + "\test_file.txt"
    f = open(path1, "r")
    info_data = f.read()
    f.close()
    s_id = info_data.split("\n")[0]
    s_pw = info_data.split("\n")[1]
except:
    print("Please enter your ID and password")
    s_id = input("ID: ")
    s_pw = input("PASSWORD: ")
    p_file = open("test_file.txt", "w")
    p_file.write(s_id + "\n" + s_pw)
    p_file.close()

print(s_id, s_pw)