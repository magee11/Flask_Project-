from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/')
def home():
    return '<h1>Home Page</h1>'


@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Role" : 'Backend',
            "Technology" : "Flask API",
        }
  
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)
