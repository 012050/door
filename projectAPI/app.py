import json

from flask import Flask, jsonify, request, render_template
from UserDataCrawler import GetUserData
app = Flask(__name__)

@app.route("/", methods=["GET"])
def MainPage():
    return render_template("home.html")

@app.route("/getdata", methods=["POST", "GET"])
def GetUserDataPage():
    ID = request.form.get("ID")
    PW = request.form.get("PASSWORD")

    # POST 요청 - 데이터 저장 및 반환
    if request.method == "POST":
        GetUserData(ID, PW)
        FileName = f'{ID}.json'
        with open(FileName, 'r') as json_file:
            json_data = json.load(json_file)
        return jsonify(json_data)

    # GET 요청 - 데이터 반환
    elif request.method == "GET":
        FileName = f'{ID}.json'
        with open(FileName, 'r') as json_file:
            json_data = json.load(json_file)
        return jsonify(json_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
