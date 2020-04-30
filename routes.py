from flask import Flask,render_template,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
@app.route('/',methods=['GET','POST'])
def fn():
    if request.method=='POST':
        mongo.db.col.insert({'name': request.form['name']})
    return render_template('index.html')
@app.route('/registration')
def reg():
    return render_template('form.html')
@app.route('/login')
def log():
    return render_template('log.html')
if __name__=='__main__':
    app.run(debug=True)