from flask import Flask,render_template
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def fn():
    return render_template('index.html')
@app.route('/registration')
def reg():
    return render_template('form.html')
@app.route('/login')
def log():
    return render_template('log.html')
if __name__=='__main__':
    app.run(debug=True)