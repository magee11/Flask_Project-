import traceback
import json
from flask import Flask,jsonify,request
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer,DateTime,Boolean


app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Curd.sqlite3'

db = SQLAlchemy(app)

ma = Marshmallow(app)

class  Todolist(db.Model):
   id = Column(Integer,primary_key=True)
   name = Column(String(200),nullable = False)
   descriptions = Column(String(200),nullable = False)
   complete = Column(Boolean, nullable = True)  
   date_created =Column(DateTime, default = datetime.utcnow)


# def __repr__(self):
#     return self.id

db.create_all()

class TodolistSchema(ma.Schema):
    class Meta:
        fields = ('name','descriptions','complete','date_created')

todolist_schema = TodolistSchema(many = False)
todolists_schema = TodolistSchema(many = True)

@app.route('/todolist', methods=['POST'])
def add_todolist():

    try:
        name = request.json['name']
        descriptions = request.json['descriptions']
        complete = request.json['complete']
        date_created = datetime.utcnow()

        new_todo  = Todolist()
        new_todo.name = name
        new_todo.descriptions = descriptions 
        new_todo.complete = complete
        new_todo.date_created = date_created


        db.session.add(new_todo)
        db.session.commit() 

        return todolist_schema.jsonify(new_todo)

    except Exception as e:
        print(traceback.print_exc())
        return jsonify({"Error":"invalid request."})     
        # return todolist_schema.jsonify(new_todo)


if __name__ == "__main__":
    app.run(debug=True)
