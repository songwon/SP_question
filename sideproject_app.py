from flask import Flask
app = Flask("my flask app")
from flask import render_template
import json

@app.route("/home")
def home():
    return render_template("sideproject_p3.html")

@app.route("/intro")
def intro():
    return render_template("sideproject_p1.html")

@app.route("/Booklist")
def Booklist():
    return render_template("sideproject_p2.html")

@app.route("/getbook")
def getbook():
    import os
    import sys
    import urllib

    from flask import request, jsonify
    book_name = request.args.get('book_name')
    client_id = "YkADYXXhPc1UWpmh79O8"
    client_secret = "NKSNfUIXPb"

    encText = urllib.parse.quote(book_name)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        result_data = json.loads(response_body)

    else:
        print("Error Code:" + rescode)
        result_data = recode
        
    data_dict = {}
    data_dict['result'] = result_data
    return jsonify(data_dict)


app.run("0.0.0.0", port=5000, debug=True)