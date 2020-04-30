# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
# from flask_pymongo import PyMongo
from pymongo import MongoClient
app=Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
# client = MongoClient("mongodb://127.0.0.1:27017")  # host uri

client = MongoClient("mongodb://sanyam:123@cluster0-shard-00-00-6li5y.mongodb.net:27017,cluster0-shard-00-01-6li5y.mongodb.net:27017,cluster0-shard-00-02-6li5y.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


# client = MongoClient() 
# client = MongoClient(“mongodb://localhost:27017/”) 
# client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('localhost', 27017)




@app.route('/',methods=['GET','POST'])
def fn():
    if request.method=='POST':
        pt = db.col.insert_one({"name": request.form['name'],
        "username": request.form['username'],
        "psw": request.form['psw'],
        })
        return "saknya"
    return render_template('index.html')
@app.route('/registration')
def reg():
    return render_template('form.html')
@app.route('/login')
def log():
    return render_template('log.html')
if __name__=='__main__':
    app.run(debug=True)