from flask import flask
app=Flask(__name__)
@app.routes('/')
render("Hello")