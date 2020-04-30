# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from pymongo import MongoClient
import bcrypt
app=Flask(__name__)

# client = MongoClient("mongodb://sanyam:123@cluster0-shard-00-00-6li5y.mongodb.net:27017,cluster0-shard-00-01-6li5y.mongodb.net:27017,cluster0-shard-00-02-6li5y.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
# client = MongoClient("mongodb://sanyam:123@cluster0-shard-00-00-6li5y.mongodb.net:27017,cluster0-shard-00-01-6li5y.mongodb.net:27017,cluster0-shard-00-02-6li5y.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
client = MongoClient("mongodb://sanyam:123@cluster0-shard-00-00-6li5y.mongodb.net:27017,cluster0-shard-00-01-6li5y.mongodb.net:27017,cluster0-shard-00-02-6li5y.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

@app.route('/',methods=['GET','POST'])
def fn():
    if request.method=='POST':
        passwor=request.form['psw']
        hashed = bcrypt.hashpw(passwor.encode('utf-8'), bcrypt.gensalt())
        pt = db.col.insert_one({"name": request.form['name'],
        "username": request.form['username'],
        "psw": hashed,
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