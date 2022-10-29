from flask import Flask, jsonify, redirect, render_template, url_for, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/user')
def usercenter():
    if request.method == "GET":
        return render_template('usercenter.html')

if __name__ == '__main__':
    app.run(debug=True)