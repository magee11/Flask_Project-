from crypt import methods
from unicodedata import name
from urllib import request
from flask import Flask,request,json,jsonify
import json

app = Flask(__name__)

@app.route('/service', methods=['POST','GET'])
def home():
    data = json.loads(request.data)
    name = data.get("name")
    age = data.get("age")

    json_object = json.dumps(data, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    return jsonify({"name":name,"age":age})

if __name__ ==('__main__'):
    app.run(debug=True)
