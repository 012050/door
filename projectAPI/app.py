import os
import dotenv
import time
import json

from flask import Flask, jsonify, request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


dotenv.load_dotenv(dotenv.find_dotenv())

# ID = os.environ["ID"]
# PW = os.environ["PW"]

app = Flask(__name__)

json_data = {"test": "test"}

@app.route("/getdata", methods=["GET"])
def UserDataSend():
    return jsonify(json_data)

@app.route("/getdata", methods=["POST"])
def UserDataGet():
    ID = request.form.get("ID")
    PW = request.form.get("PASSWORD")
    driver = webdriver.Chrome()
    driver.close()
    return 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)